from server.books.models import Book
from server.users.models import UserProfile


# Function to get a book by its primary key
def get_book(pk):
    try:
        book = Book.objects.get(pk=pk)
        return book
    except Book.DoesNotExist:
        return None


# Function to get all books owned by a user
def get_all_books_by_user(user):
    try:
        user_profile = user.userprofile
        all_books = Book.objects.filter(owner=user_profile)
        return all_books
    except UserProfile.DoesNotExist:
        return None
