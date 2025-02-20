from django.contrib import admin


from .models import Author, Book, Library, Librarian

# Customizing Admin Display
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show ID and Name in the admin list view
    search_fields = ('name',)  # Enable search by name

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')  # Show book details
    list_filter = ('author',)  # Filter books by author
    search_fields = ('title', 'author__name')  # Search by book title or author name

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show library name
    filter_horizontal = ('books',)  # Provides a better UI for ManyToMany relationships

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'library')  # Show librarian details
    search_fields = ('name', 'library__name')  # Search by librarian name or library name

# Registering Models
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)
