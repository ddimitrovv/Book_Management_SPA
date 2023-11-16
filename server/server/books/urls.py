from django.urls import path

from server.books.views import create_book, details_book, all_books_by_category, BookDeleteView, BookUpdateView

urlpatterns = [
    path('', all_books_by_category, name='all_book_by_category'),
    path('create/', create_book, name='create-book'),
    path('<int:book_pk>/', details_book, name='details_book'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='update_book'),
    path('<int:id>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
