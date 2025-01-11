from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        # it is list because we created form
        fields = ['text', 'photo']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # it is a tuple because it is built in form
        fields = ('username', 'email', 'password1', 'password2')