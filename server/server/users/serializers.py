from django.contrib.auth import get_user_model
from rest_framework import serializers
from server.users.models import UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    This serializer is used for creating new user instances during registration.

    Fields:
    - username (str): The username for the new user.
    - email (str): The email address for the new user.
    - password (str): The password for the new user.

    Additional Info:
    - The password field is write-only for security.

    Methods:
    - create: Create and return a new user instance.
    """

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a new user instance.

        Parameters:
        - validated_data (dict): Validated data for creating the new user.

        Returns:
        - User: The newly created user instance.
        """

        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    This serializer is used for validating user login credentials.

    Fields:
    - username (str): The username for login.
    - password (str): The password for login.

    Methods:
    - validate: Validate the provided credentials and return user data if valid.

    Raises:
    - serializers.ValidationError: If the credentials are invalid.
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validate the provided credentials.

        Parameters:
        - data (dict): The input data containing username and password.

        Returns:
        - dict: The validated data containing the user instance.

        Raises:
        - serializers.ValidationError: If the credentials are invalid.
        """

        user = get_user_model().objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            data['user'] = user
            return data
        raise serializers.ValidationError('Invalid credentials')


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model.

    This serializer is used for representing CustomUser instances.

    Fields:
    - id (int): The user ID.
    - username (str): The username of the user.
    - email (str): The email address of the user.
    """

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile model.

    This serializer is used for representing UserProfile instances.

    Fields:
    - All fields from the UserProfile model excluding the 'user' field.
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating UserProfile.

    This serializer is used for updating UserProfile instances.

    Fields:
    - All fields from the UserProfile model excluding the 'user' field.

    Additional Info:
    - The 'user' field is excluded to prevent direct user manipulation during updates.
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)
