from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from server.books.models import Book
from server.books.operations import get_book
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


class BooksByStatusPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class AllBooksByCategory(APIView):
    """
    API view to retrieve all books grouped by their status for the authenticated user.

    Requires TokenAuthentication.

    Methods:
    - get: Retrieves and returns all books grouped by status for the authenticated user.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = BooksByStatusPagination

    def get(self, request, book_status, *args, **kwargs):
        """
        Handles HTTP GET requests to retrieve all books by a certain status.

        Parameters:
        - request: The HTTP request object.
        - book_status: The status of the books to retrieve.
        - *args: Additional positional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - Response: Serialized data containing books by status with pagination.
        """

        user = request.user

        if user.is_authenticated:
            books = Book.objects.filter(owner=user.pk, status=book_status)

            paginator = BooksByStatusPagination()
            result_page = paginator.paginate_queryset(books, request)

            serialized_books = BookSerializer(result_page, many=True).data

            return paginator.get_paginated_response(serialized_books)
        else:
            return Response({'detail': 'User not authenticated'}, status=book_status.HTTP_401_UNAUTHORIZED)


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
