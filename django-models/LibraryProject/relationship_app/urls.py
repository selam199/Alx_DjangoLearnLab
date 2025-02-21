from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
from .views import admin_view, librarian_view, member_view
from . import views

urlpatterns = [
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
    path("books/", list_books, name="list_books"),  # URL for function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # URL for class-based view
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
