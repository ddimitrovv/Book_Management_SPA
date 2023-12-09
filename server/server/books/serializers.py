from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from server.books.models import Book, BookRating
from server.users.operations import get_user_profile


class AverageRatingField(serializers.Field):
    """
    Custom serializer field to calculate and represent the average rating of a book.
    """

    def to_representation(self, value):
        ratings_queryset = value.book_ratings.all()

        if ratings_queryset:
            average_rating = sum(rating.rating for rating in ratings_queryset) / len(ratings_queryset)
            return round(average_rating, 2)
        return 0.00


class BookSerializerRequestUserIsOwner(serializers.ModelSerializer):
    """
    Serializer for the Book model, including the 'average_rating' field.

    Attributes:
    - average_rating: Custom field to represent the average rating of the book.

    Example:
    ```
    serializer = BookSerializer(book_instance)
    data = serializer.data
    ```

    Meta:
    - model: The Book model.
    - exclude: Excludes the 'owner' field from the serialization.
    """

    average_rating = AverageRatingField(source='*')

    class Meta:
        model = Book
        exclude = ('owner', 'ratings',)


class BookSerializerRequestUserIsNotOwner(serializers.ModelSerializer):
    """
    Serializer for the Book model, including the 'average_rating' field.

    Attributes:
    - average_rating: Custom field to represent the average rating of the book.

    Example:
    ```
    serializer = BookSerializer(book_instance)
    data = serializer.data
    ```

    Meta:
    - model: The Book model.
    - exclude: Excludes the 'owner' field from the serialization.
    """

    average_rating = AverageRatingField(source='*')

    class Meta:
        model = Book
        exclude = ('owner', 'ratings', 'status',)


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
        exclude = ('ratings',)

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


class BookRatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookRating model.

    Fields:
    - userprofile (PrimaryKeyRelatedField): The user who rated the book.
    - book (PrimaryKeyRelatedField): The book that is being rated.
    - rating (PositiveIntegerField): The rating given by the user.

    Validators:
    - UniqueTogetherValidator: Ensures that a user can rate a book only once.
    """

    class Meta:
        model = BookRating
        fields = ['userprofile', 'book', 'rating']

        validators = [
            UniqueTogetherValidator(
                queryset=BookRating.objects.all(),
                fields=['userprofile', 'book'],
                message='You have already rated this book.'
            )
        ]
