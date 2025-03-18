from django.urls import path
from django.contrib.auth import views as auth_views
from .views import post_detail, edit_comment, delete_comment
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
