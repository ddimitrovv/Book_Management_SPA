from rest_framework import serializers

from server.books.models import Book
from server.users.operations import get_user_profile


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('owner',)


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        user_profile = get_user_profile(self.context['request'])
        validated_data['owner'] = user_profile
        return super().create(validated_data)
