from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from server.books.operations import get_all_books_by_user
from server.books.serializers import BookSerializer
from server.users.operations import get_user_profile
from server.users.serializers import CustomUserSerializer, UserProfileSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required
def user_details(request, user_id):
    user = request.user

    if user.is_authenticated:
        user_profile = get_user_profile(request)
        books = get_all_books_by_user(user)

        return Response(
            {
                    'user': CustomUserSerializer(user).data,
                    'user_profile': UserProfileSerializer(user_profile).data,
                    'books': [BookSerializer(book).data for book in books]
            },
            status=status.HTTP_200_OK
        )
    return Response({'detail': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
