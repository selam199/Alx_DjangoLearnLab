# Create Operation

This document explains the steps to create a `Book` instance in the Django shell.

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book