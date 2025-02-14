from django.contrib import admin
from .models import Book

# Customizing the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filtering by publication year
    list_filter = ('publication_year',)

    # Enable search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)


