from django import forms
from django.forms.widgets import EmailInput, PasswordInput
from ..models.users.customer import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_qs = Customer.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError(
    #         'The email you supplied has already been used.'
    #         )
    #     return email
