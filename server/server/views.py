from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from server.books.choices import BookStatusChoices
from server.books.models import Book
from server.users.operations import get_user_profile, check_if_user_exists
from server.users.serializers import CustomUserSerializer, UserProfileSerializer
from server.users.serializers import UserRegistrationSerializer, UserLoginSerializer
from server.books.serializers import BookSerializerRequestUserIsNotOwner


class HomeView(APIView):
    """
    Home View

    If the user is logged in, this view returns detailed information including
    the user's profile, their books, and books grouped by genre. If the user is not logged in, it returns None.

    Attributes:
    - permission_classes (tuple): A tuple containing the permission classes for the view.
    """

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Retrieve user data, user profile, books, and books grouped by genre.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - Response: A response containing user, user profile, books, and books grouped by genre.
        """

        user = request.user
        if user.is_anonymous:
            data = {
                'user': None,
                'user_profile': None,
            }
        else:
            user_profile = get_user_profile(request)

            user_data = CustomUserSerializer(user).data if user else None
            user_profile_data = UserProfileSerializer(user_profile).data if user_profile else None

            data = {
                'user': user_data,
                'user_profile': user_profile_data,
            }

        # Get books grouped by genre
        all_books = Book.objects.all()
        books_by_genre = {}
        for book in all_books:
            if book.genre not in books_by_genre:
                books_by_genre[book.genre] = []
            books_by_genre[book.genre].append(BookSerializerRequestUserIsNotOwner(book).data)

        data['books_by_genre'] = books_by_genre

        return Response(data)


class MyBooksView(APIView):
    """
    This view retirns user books by status

    If the user is logged in, this view returns detailed information including
    the user's profile and their books. If the user is not logged in, it returns None.

    Attributes:
    - permission_classes (tuple): A tuple containing the permission classes for the view.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Retrieve user data, user profile, and books.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - Response: A response containing user, user profile, and books collections types.
        """

        user = request.user
        if user.is_anonymous:
            data = {
                'user': None,
                'user_profile': None,
                'status': BookStatusChoices.choices,
            }
        else:
            user_profile = get_user_profile(request)

            user_data = CustomUserSerializer(user).data if user else None
            user_profile_data = UserProfileSerializer(user_profile).data if user_profile else None

            data = {
                'user': user_data,
                'user_profile': user_profile_data,
                'status': BookStatusChoices.choices,
            }

        return Response(data)


class UserRegistrationView(APIView):
    """
    User Registration View

    Allows users to register by providing a valid set of registration data.

    Methods:
    - post: Handle the registration process when a POST request is received.

    Attributes:
    - permission_classes (tuple): A tuple containing the permission classes for the view.
    """

    def post(self, request, *args, **kwargs):
        """
        Register a new user.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - JsonResponse: A JSON response indicating the result of user registration.
        """

        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {'user': CustomUserSerializer(user).data, 'token': token.key},
                status=status.HTTP_201_CREATED
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    User Login View

    Allows users to log in by providing valid login credentials.

    Methods:
    - post: Handle the login process when a POST request is received.

    Attributes:
    - permission_classes (tuple): A tuple containing the permission classes for the view.
    """

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        """
        Log in a user.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - Response: A response containing user data and token upon successful login.
        """

        user = check_if_user_exists(request)
        if user is None:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                """Log in the user"""
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)

                """Return user and token"""
                return Response(
                    {'user': CustomUserSerializer(user).data, 'token': token.key},
                    status=status.HTTP_200_OK
                )

            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """
    User Logout View

    Allows authenticated users to log out.

    Methods:
    - get: Handle the logout process when a GET request is received.
    """

    def get(self, request, *args, **kwargs):
        """
        Log out a user.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - JsonResponse: A JSON response indicating the result of user logout.
        """

        if request.user.is_authenticated:
            request.auth.delete()
            logout(request)
            return JsonResponse({'detail': 'User logged out successfully'}, status=200)
        else:
            return JsonResponse({'detail': 'User is not authenticated'}, status=401)
