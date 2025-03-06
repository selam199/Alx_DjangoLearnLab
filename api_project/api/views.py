from rest_framework.generics import ListAPIView
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Use the Book model as the queryset
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
