from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=28, required=False, help_text='First Name')
    surname = forms.CharField(max_length=28, required=False, help_text='Surname')
    email = forms.CharField(max_length=50, required=False, help_text='email')
    password = forms.CharField(min_length=8, max_length=12, required=False, help_text='password')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'surname', 'email', 'password')
