from django.forms import ModelForm
from django import forms
from django.forms.widgets import EmailInput, PasswordInput
from ..models.users.customer import Customer


class SignUpForm(ModelForm):
    firstname = forms.CharField(max_length=28, required=False)
    surname = forms.CharField(max_length=28, required=False)
    email = forms.CharField(max_length=50, required=False, widget=EmailInput)
    password = forms.CharField(
        min_length=8, max_length=12, required=False, widget=PasswordInput)

    class Meta:
        model = Customer
        fields = ['firstname', 'surname', 'email', 'password']
