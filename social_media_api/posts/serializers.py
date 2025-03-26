from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id', 'username', 'email']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'post', 'author', 'created_at', 'updated_at']
    
    def validate_content(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Comment must be at least 5 characters long.")
        return value

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 
            'author', 
            'title', 
            'content', 
            'created_at', 
            'updated_at', 
            'comments',
            'comment_count'
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'comments']
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        if len(value) > 255:
            raise serializers.ValidationError("Title cannot exceed 255 characters.")
        return value
    
    def validate_content(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Post content must be at least 10 characters long.")
        return value

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(author=user, **validated_data)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
    
    def create(self, validated_data):
        user = self.context['request'].user
        post = self.context['post']
        return Comment.objects.create(
            author=user,
            post=post,
            **validated_data
        )