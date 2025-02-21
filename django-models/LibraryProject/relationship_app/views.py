from django.shortcuts import render,HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test



# Helper function to check user role
def check_role(role):
    def inner_function(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return inner_function

# View for Admin
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# View for Librarian
@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# View for Member
@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')




# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("login")  # Redirect to login page
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})
# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"  # Use "library" in templates
    
    
