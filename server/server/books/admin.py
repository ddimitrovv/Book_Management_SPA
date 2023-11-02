from django.contrib import admin

from server.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'status', 'rating', 'price', 'owner']
    search_fields = ['name', 'owner__user__username']
    search_help_text = 'Search book by book name or owner name'
