from django.db import models
from django.contrib.auth.models import User  # Importing the User model

class Post(models.Model):
    # Title of the post, a character field with a maximum length of 200 characters
    title = models.CharField(max_length=200)
    
    # Content of the post, a text field to allow for large amounts of text
    content = models.TextField()
    
    # Published date, automatically set when a post is created
    published_date = models.DateTimeField(auto_now_add=True)
    
    # Foreign key to link each post to a user (author), assuming one user can have many posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # Optional: Add a string representation for the model to return the title of the post
    def __str__(self):
        return self.title

    # Optional: You can also add a method to return a short preview of the post
    def get_preview(self):
        # Return the first 100 characters of the content
        return self.content[:100] + '...'


