from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, register, profile, profile_update

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),

    # Comment URLs
    # Create a new comment on a post
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),

    # Edit an existing comment
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),

    # Delete a comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]

    





    