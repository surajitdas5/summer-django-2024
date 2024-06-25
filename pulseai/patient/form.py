from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Blog
from patient.models import HeartVital

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', "last_name", "username", "email", "password1", "password2"]


class HeartVitalForm(ModelForm):
    class Meta:
        model = HeartVital
        # fields = '__all__'
        exclude = ['user', 'heart_disease', 'prediction_probability']