from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

from server.users.models import CustomUser
from server.users.serializers import UserRegistrationSerializer, UserLoginSerializer, CustomUserSerializer


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
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'user': CustomUserSerializer(user).data,
                    'token': token.key
                }, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
