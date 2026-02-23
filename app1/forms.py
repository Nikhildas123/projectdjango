from django import forms
from .models import book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model=book
        fields=['title','author','price','pub_date','description']
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
