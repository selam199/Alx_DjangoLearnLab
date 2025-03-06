from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Use the Book model as the queryset
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    