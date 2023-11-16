from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from server.books.operations import get_all_books_by_user
from server.books.serializers import BookSerializer
from server.users.operations import get_user_profile, get_user_object
from server.users.serializers import CustomUserSerializer, UserProfileSerializer
from server.users.models import CustomUser
from server.users.serializers import UserRegistrationSerializer, UserLoginSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = get_user_profile(request)
        books = get_all_books_by_user(user=user)
    else:
        user = None
        user_profile = None
        books = None

    user_data = CustomUserSerializer(user).data if user else None
    user_profile_data = UserProfileSerializer(user_profile).data if user_profile else None
    books_data = {book.pk: BookSerializer(book).data for book in books} if books else None

    data = {
        'user': user_data,
        'user_profile': user_profile_data,
        'books': books_data,
    }

    return JsonResponse(data)


@api_view(['POST'])
def user_registration(request):

    if request.method == 'POST':
        request_data = request.data
        serializer = UserRegistrationSerializer(data=request_data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            email = serializer.validated_data.get('email')

            if not username or not password or not email:
                return Response(
                    {'error': 'Please provide username, password, and email.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Create the user
            user = CustomUser.objects.create_user(username=username, password=password, email=email)

            # Log in the user
            login(request, user)

            # Create a dictionary with the data to return
            response_data = {
                'message': 'User created successfully',
                'user': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        user = get_user_object(request)
        if not user:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                token, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {'user': CustomUserSerializer(user).data, 'token': token.key},
                    status=status.HTTP_200_OK
                )
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required()
def user_logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # Logout the user
            logout(request)
            return Response({'detail': 'User logged out successfully'}, status=status.HTTP_200_OK)

    return Response({'detail': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
