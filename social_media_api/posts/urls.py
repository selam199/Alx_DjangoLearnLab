from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from posts.views import PostViewSet, CommentViewSet
from accounts.views import UserFeedView

# Create a base router for posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Create a nested router for comments
posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    # Include both router URLs
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    
    # Additional custom endpoints
    path('posts/user_posts/', PostViewSet.as_view({'get': 'user_posts'}), name='user-posts'),
    
     path('feed/', UserFeedView.as_view(), name='user-feed'),
]