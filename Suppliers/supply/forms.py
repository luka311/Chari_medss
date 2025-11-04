from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from unicodedata import category

from .models import ContactMessage
from .models import Product
from .models import Review

# Signup form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Login form
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

# Contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'image', 'description']


class ReviewForm(forms.ModelForm):
   class Meta:
      model = Review
      fields = ['name', 'message']
