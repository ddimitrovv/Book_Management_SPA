"""Books urls"""
from django.urls import path

from server.books.views import CreateBook, DetailsBook, AllBooksByCategory, BookDeleteView, BookUpdateView

urlpatterns = [
    path('<str:status>/', AllBooksByCategory.as_view(), name='books-by-status'),
    path('create/', CreateBook.as_view(), name='create-book'),
    path('<int:book_pk>/', DetailsBook.as_view(), name='details_book'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='update_book'),
    path('<int:id>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
