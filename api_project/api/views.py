from rest_framework import generics
from rest_framework import viewsets 
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Use the Book model as the queryset
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Apply permissions: Only authenticated users can access
    permission_classes = [IsAuthenticated]
    