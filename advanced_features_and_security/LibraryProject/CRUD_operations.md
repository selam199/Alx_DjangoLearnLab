 from bookshelf.models import Book
>>>
>>> # Create a book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984>
>>> #### **4.2 Retrieve the Book instance**
>>> ```python
  File "<console>", line 1
    ```python
    ^
SyntaxError: invalid syntax
>>> # Retrieve the book
>>> book = Book.objects.get(title="1984")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Program Files\Python313\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python313\Lib\site-packages\django\db\models\query.py", line 652, in get
    raise self.model.MultipleObjectsReturned(
    ...<5 lines>...
    )
bookshelf.models.Book.MultipleObjectsReturned: get() returned more than one Book -- it returned 2!
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)
>>> # Update the title
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four>
>>> # Delete the book
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> # Output: (1, {'bookshelf.Book': 1})
>>>
>>> # Confirm deletion
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>
>>> Book.bjects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Book' has no attribute 'bjects'. Did you mean: 'objects'?
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984>
>>> Book.objects.all()
<QuerySet [<Book: 1984>, <Book: 1984>]>
