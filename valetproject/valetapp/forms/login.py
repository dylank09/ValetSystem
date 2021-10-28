from django.forms import ModelForm
from django import forms
from ..models.users.customer import Customer

class LoginForm(ModelForm):
    email = forms.CharField(max_length=50, required=False)
    password = forms.CharField(min_length=8, max_length=12, required=False)


    class Meta:
        model = Customer
        fields = ['email', 'password']
