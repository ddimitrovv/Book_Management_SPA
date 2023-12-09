from django.contrib import admin
from django.db.models import Avg

from server.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.

    Attributes:
    - list_display (list): Fields to display in the list view.
    - search_fields (list): Fields to use in the admin search.
    - list_filter (list): Fields to use as filters in the right sidebar.
    """

    search_fields = ['name', 'owner__user__username']
    search_help_text = 'Search book by book name or owner name'
    list_display = ['name', 'author', 'display_average_rating', 'status', 'price', 'owner']

    def display_average_rating(self, obj):
        average_rating = obj.book_ratings.aggregate(Avg('rating'))['rating__avg']

        return f'{average_rating:.2f}' if average_rating is not None else 'N/A'

    display_average_rating.short_description = 'Average Rating'
