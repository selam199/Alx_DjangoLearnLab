import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_projects.settings")  # Replace 'your_project' with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")

def list_books_in_library(library_name):
    """
    List all books in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books available in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian assigned to a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using related_name from OneToOneField
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")

if __name__ == "__main__":
    # Example Queries
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
