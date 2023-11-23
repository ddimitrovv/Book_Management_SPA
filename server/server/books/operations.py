from server.books.models import Book
from server.users.models import UserProfile


def get_book(pk):
    """
    Retrieve a book from the database by its primary key.

    :param int pk: The primary key of the book to retrieve.
    :return: The Book instance if found, otherwise None.
    :rtype: Book or None
    """

    try:
        book = Book.objects.get(pk=pk)
        return book
    except Book.DoesNotExist:
        return None


def get_all_books_by_user(user):
    """
    Retrieve all books owned by a given user.

    :param User user: The user for whom to retrieve owned books.
    :return: A queryset containing all books owned by the user, or None if the user profile does not exist.
    :rtype: QuerySet[Book] or None
    """

    try:
        user_profile = user.userprofile
        all_books = Book.objects.filter(owner=user_profile)
        return all_books
    except UserProfile.DoesNotExist:
        return None
