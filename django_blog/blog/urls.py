from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
    # ... other view imports ...
)
from . views import register, profile, profile_update
urlpatterns = [
    # Authentication and Profile URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    
    # Existing Comment URLs
    
    # Blog post URLs
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/new/", PostCreateView.as_view(), name="post_new"),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    
    
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]






    