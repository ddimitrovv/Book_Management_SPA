"""Books urls"""
from django.urls import path

from server.books.views import CreateBook, DetailsBook, AllBooksByCategory, BookDeleteView, BookUpdateView, RateBook

urlpatterns = [
    path('create/', CreateBook.as_view(), name='create-book'),
    path('<str:book_status>/', AllBooksByCategory.as_view(), name='books-by-status'),
    path('details/<int:book_pk>/', DetailsBook.as_view(), name='details_book'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='update_book'),
    path('delete/<int:id>/', BookDeleteView.as_view(), name='book-delete'),
    path('rate-book/<int:book_pk>/', RateBook.as_view(), name='book-rate'),
]
