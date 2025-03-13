from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It serializes all fields of the Book model.
    Includes a validation method to ensure that the publication year is not in the future.
    """
    
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        If the provided year is greater than the current year, it raises a ValidationError.
        """
        
        """Ensure publication year is not in the future"""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    
    """
    Serializer for the Author model.
    It includes:
    - The author's name.
    - A nested BookSerializer to serialize the books associated with the author.
    The books field is read-only to prevent book creation through this serializer.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['name', 'books']
"""
    Relationship Handling:
    - The ForeignKey in the Book model establishes a one-to-many relationship with the Author model.
    - In the AuthorSerializer, the books field is serialized using the BookSerializer.
    - The related_name='books' in the Book model allows the Author model to access related books.
    - read_only=True ensures that books cannot be added or updated via the AuthorSerializer.
    """