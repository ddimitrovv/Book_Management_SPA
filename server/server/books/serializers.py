from rest_framework import serializers
from server.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('owner',)
