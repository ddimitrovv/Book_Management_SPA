from django.urls import path

from server.books.views import create_book, details_book, all_books_by_category

urlpatterns = [
    path('create/', create_book, name='create-book'),
    path('<int:book_pk>/', details_book, name='details_book'),
    path('all/', all_books_by_category, name='all_book_by_category')
]
