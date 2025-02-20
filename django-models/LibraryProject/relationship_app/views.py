from django.shortcuts import render,HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"  # Use "library" in templates