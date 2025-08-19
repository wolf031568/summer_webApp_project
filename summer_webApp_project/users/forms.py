from django import forms
from .models import users

#define forms for user registration and login 
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = users
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField() #gets and verifies user email
    password = forms.CharField(widget=forms.PasswordInput)
