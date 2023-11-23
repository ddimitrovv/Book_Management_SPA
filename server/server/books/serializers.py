from rest_framework import serializers

from server.books.models import Book
from server.users.operations import get_user_profile


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, excluding the 'owner' field.

    Attributes:
    - Meta: Metadata class defining the model and excluded fields.
    """

    class Meta:
        model = Book
        exclude = ('owner',)


class BookCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new Book instance.

    This serializer allows creating a new Book instance by including all fields.
    The 'owner' field is automatically set to the authenticated user.

    Attributes:
    - Meta: Metadata class defining the model and included fields.
    - create: Custom method to set the 'owner' field based on the authenticated user.

    Example:
    ```
    serializer = BookCreateSerializer(data=request_data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    ```
    """

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new Book instance with the 'owner' field set to the authenticated user.

        Parameters:
        - validated_data (dict): Validated data for creating the Book instance.

        Returns:
        - Book: The newly created Book instance.
        """

        user_profile = get_user_profile(self.context['request'])
        validated_data['owner'] = user_profile
        return super().create(validated_data)
