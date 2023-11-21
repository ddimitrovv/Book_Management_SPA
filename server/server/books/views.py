from django.db.models import Count

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from server.books.models import Book
from server.books.operations import get_book, get_all_books_by_user
from server.books.permissions import IsOwner
from server.books.serializers import BookCreateSerializer, BookSerializer
from server.users.operations import get_user_profile


class CreateBook(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = get_user_profile(request).pk
        serializer = BookCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsBook(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    def get(self, request, book_pk, *args, **kwargs):
        book = get_book(book_pk)
        if book:
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllBooksByCategory(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:
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


class BookUpdateView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
