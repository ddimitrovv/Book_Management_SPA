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
    """
    API view to create a new book associated with the authenticated user.

    Requires TokenAuthentication for user authentication.

    Methods:
    - post: Creates a new book instance and associates it with the authenticated user.
            Returns a response with the serialized book data upon success.
            Returns an error response if the input data is invalid.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Handles HTTP POST requests to create a new book.

        Parameters:
        - request: The HTTP request object.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - Response: Serialized book data or error response.
        """

        request.data['owner'] = get_user_profile(request).pk
        serializer = BookCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsBook(APIView):
    """
    API view to retrieve details of a specific book for the authenticated user.

    Requires TokenAuthentication and ownership permission.

    Methods:
    - get: Retrieves and returns the details of the specified book.
            Returns a 404 response if the book is not found or if the user does not own the book.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    def get(self, request, book_pk, *args, **kwargs):
        """
        Handles HTTP GET requests to retrieve details of a specific book.

        Parameters:
        - request: The HTTP request object.
        - book_pk: Primary key of the book to retrieve.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - Response: Serialized book data or a 404 response if the book is not found.
        """

        book = get_book(book_pk)
        if book:
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllBooksByCategory(APIView):
    """
    API view to retrieve all books grouped by their status for the authenticated user.

    Requires TokenAuthentication.

    Methods:
    - get: Retrieves and returns all books grouped by status for the authenticated user.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Handles HTTP GET requests to retrieve all books grouped by status.

        Parameters:
        - request: The HTTP request object.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - Response: Serialized data containing books grouped by status.
        """

        user = request.user

        if user.is_authenticated:
            books = get_all_books_by_user(user)
            """Grouping books by status"""
            books_by_status = books.values('status').annotate(total=Count('status'))

            """To fetch the result as a dictionary with status as keys and a list of books as values"""
            book_status_dict = {stat['status']: list(Book.objects.filter(owner=user.pk, status=stat['status'])) for stat
                                in books_by_status}
            response_data = {'books': {}}

            """Serializing books for each status and organizing them in the response data"""
            for stat, books in book_status_dict.items():
                serialized_books = BookSerializer(books, many=True).data
                response_data['books'][stat] = serialized_books

            return Response(response_data, status=status.HTTP_200_OK)


class BookUpdateView(RetrieveUpdateAPIView):
    """
    API view to update a specific book for the authenticated user.

    Requires TokenAuthentication and ownership permission.

    Methods:
    - patch: Updates the specified book and returns the serialized updated data.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    def patch(self, request, *args, **kwargs):
        """
        Handles HTTP PATCH requests to update a specific book.

        Parameters:
        - request: The HTTP request object.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - Response: Serialized updated book data.
        """

        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a specific book for the authenticated user.

    Requires TokenAuthentication and ownership permission.

    Methods:
    - destroy: Deletes the specified book and returns a success response.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        """
        Handles HTTP DELETE requests to delete a specific book.

        Parameters:
        - request: The HTTP request object.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - Response: Success response indicating that the book was deleted.
        """

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
