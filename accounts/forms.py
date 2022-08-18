from django import forms
from .models import Register
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Register
        fields = ('username',  'email', 'password1', 'password2')

