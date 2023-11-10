from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.decorators.http import require_POST

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status

from server.books.models import Book
from server.books.operations import get_book, get_all_books_by_user
from server.books.serializers import BookCreateSerializer, BookSerializer
from server.users.operations import get_user_profile


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@require_POST
@login_required
def create_book(request, user_pk):
    if request.method == 'POST':
        request.data['owner'] = get_user_profile(request).pk
        serializer = BookCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required
def details_book(request, book_pk):
    book = get_book(book_pk)
    if book:
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required
def all_books_by_category(request, user_id):
    user = request.user

    if user.is_authenticated and user_id == user.pk:
        books = get_all_books_by_user(user)
        # Grouping books by status
        books_by_status = books.values('status').annotate(total=Count('status'))

        # To fetch the result as a dictionary with status as keys and a list of books as values
        book_status_dict = {stat['status']: list(Book.objects.filter(owner=user.pk, status=stat['status'])) for stat
                            in books_by_status}
        response_data = {'books': {}}

        # Serializing books for each status and organizing them in the response data
        for stat, books in book_status_dict.items():
            serialized_books = BookSerializer(books, many=True).data
            response_data['books'][stat] = serialized_books

        return Response(response_data, status=status.HTTP_200_OK)
    return Response({'detail': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
