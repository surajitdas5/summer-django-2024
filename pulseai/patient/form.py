from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', "last_name", "username", "email", "password1", "password2"]