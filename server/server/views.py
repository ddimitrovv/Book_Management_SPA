from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from server.books.operations import get_all_books_by_user
from server.books.serializers import BookSerializer
from server.users.operations import get_user_profile, check_if_user_exists
from server.users.serializers import CustomUserSerializer, UserProfileSerializer
from server.users.serializers import UserRegistrationSerializer, UserLoginSerializer


class HomeView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            data = {
                'user': None,
                'user_profile': None,
                'books': None,
            }
        else:
            user_profile = get_user_profile(request)
            books = get_all_books_by_user(user=user)

            user_data = CustomUserSerializer(user).data if user else None
            user_profile_data = UserProfileSerializer(user_profile).data if user_profile else None
            books_data = {book.pk: BookSerializer(book).data for book in books} if books else None

            data = {
                'user': user_data,
                'user_profile': user_profile_data,
                'books': books_data,
            }

        return Response(data)


class UserRegistrationView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        user = check_if_user_exists(request)
        if user is None:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                token, _ = Token.objects.get_or_create(user=user)

                # Return both user data and token
                return Response(
                    {'user': CustomUserSerializer(user).data, 'token': token.key},
                    status=status.HTTP_200_OK
                )

            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request.auth.delete()
            logout(request)
            return JsonResponse({'detail': 'User logged out successfully'}, status=200)
        else:
            return JsonResponse({'detail': 'User is not authenticated'}, status=401)
