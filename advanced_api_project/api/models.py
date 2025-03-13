from django.db import models

# Create your models here.
class Author(models.Model):
    """
The Author model is designed to represent an individual who writes books. 
This model serves as a way to capture and manage information related to book authors. 
Each author is characterized by having a distinct and unique name that serves as their identifier, 
ensuring that no two authors within the system share the same name.
"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
The Book model is designed to represent an individual book written by a specific author. 
This model captures important details about each book, including its title and the year it was published. 
Additionally, the model includes a foreign key, which establishes a connection to the Author model. 
This foreign key represents a one-to-many relationship, meaning that a single author can be associated with multiple books. 
This relationship ensures that each book is linked to the correct author, allowing for organized and meaningful data representation.
"""

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year} by {self.author.name})"
