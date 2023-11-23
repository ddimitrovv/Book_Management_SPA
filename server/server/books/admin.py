from django.contrib import admin

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

    list_display = ['name', 'author', 'status', 'rating', 'price', 'owner']
    search_fields = ['name', 'owner__user__username']
    search_help_text = 'Search book by book name or owner name'
