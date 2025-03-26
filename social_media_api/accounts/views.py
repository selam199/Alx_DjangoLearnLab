from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, ProfileSerializer
from django.shortcuts import get_object_or_404
from .models import CustomUser
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics, permissions


User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 
                            'user': UserSerializer(user).data}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Handles user authentication and token retrieval
    """
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.id,  # Using numeric ID here
                'username': user.username,
                'email': user.email,
                'token': token.key
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

# Profile View
class ProfileView(APIView):
    """
    Handles user profile retrieval and updates
    """
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(
            request.user, 
            data=request.data, 
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    

    def post(self, request, user_id):
            user_to_follow = get_object_or_404(CustomUser, id=user_id)
        
            if request.user == user_to_follow:
                return Response(
                {"error": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
            request.user.following.add(user_to_follow)
            return Response(
                {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response(
            {"message": f"You have unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )
        
class UserFeedView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get posts from users the current user follows
        followed_users = request.user.following.all()
        feed_posts = Post.objects.filter(
            author__in=followed_users
        ).order_by('-created_at')
        
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)