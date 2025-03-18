from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import post_detail, edit_comment, delete_comment
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    
    path('posts/', views.CommentCreateView.as_view(), name='post-list'),
    path("posts/<int:pk>/edit/", views.CommentUpdateView.as_view(), name='post-edit'),
    path("post/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='post-delete'),
    
    
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    

]



    