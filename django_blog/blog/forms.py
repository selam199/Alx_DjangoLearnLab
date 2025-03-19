from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Comment
from .models import Post
from taggit.forms import TagWidget  

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class PostForm(forms.ModelForm):
    #tags = forms.CharField(required=False, help_text="Comma-separated tags")
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {  
            'tags': TagWidget(attrs={'class': 'form-control'}),  # ✅ Add TagWidget
        }
        
    def save(self, commit=True):
        post = super().save(commit=False)
        tags = self.cleaned_data.get('tags')
        if commit:
            post.save()
            if tags:
                post.tags.set(*[tag.strip() for tag in tags.split(',')])
        return post