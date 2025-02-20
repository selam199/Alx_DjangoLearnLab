from django.db import models


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book Model (One-to-Many Relationship with Author)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author.name}"


# Library Model (Many-to-Many Relationship with Books)
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


# Librarian Model (One-to-One Relationship with Library)
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return f"{self.name} (Librarian of {self.library.name})"
