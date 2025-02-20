import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()  # Ensure author exists
    if author:
        books = Book.objects.filter(author=author)  # ✅ Required Query
        return books
    return []

# List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()  # ManyToMany relationship
    return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return Librarian.objects.filter(library=library).first()  # OneToOne relationship
    return None

# Example usage (Testing the queries)
if __name__ == "__main__":
    print("Books by George Orwell:", list(get_books_by_author("George Orwell")))
    print("Books in City Library:", list(get_books_in_library("City Library")))
    print("Librarian of City Library:", get_librarian_for_library("City Library"))

