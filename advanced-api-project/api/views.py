from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

class BookListView(generics.ListCreateAPIView):
    """
    GET: Retrieve all books
    POST: Create a new book (Authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Read for all, Write for authenticated users

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a book by ID
    PUT: Update an existing book (Authenticated users only)
    DELETE: Remove a book (Authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsoOwnerOrReadOnly]

# CreateView: Add a new book
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books
    
    def perform_create(self, serializer):
        # Example of custom handling, e.g., setting the user who created the book
        serializer.save(user=self.request.user)

# UpdateView: Modify an existing book
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Only authenticated users can update books
    
    def perform_update(self, serializer):
        # Custom handling before saving the update
        serializer.save(user=self.request.user)  # Example

# DeleteView: Remove a book
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete books