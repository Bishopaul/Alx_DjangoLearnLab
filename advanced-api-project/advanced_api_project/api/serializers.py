from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


# BookSerializer handles serialization of Book objects.
# Includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer serializes Author objects.
# Includes a nested BookSerializer to show all books written by the author.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to show related books dynamically.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
