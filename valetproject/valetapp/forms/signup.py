from django.forms import ModelForm
from django import forms
from django.forms.widgets import EmailInput, PasswordInput
from ..models.users.customer import Customer
from django.contrib.auth import get_user_model


class SignUpForm(ModelForm):
    firstname = forms.CharField(max_length=28, required=False)
    surname = forms.CharField(max_length=28, required=False)
    email = forms.EmailField(max_length=50, required=False, widget=EmailInput)
    password = forms.CharField(
        min_length=8, max_length=12, required=False, widget=PasswordInput)

    class Meta:
        model = Customer
        fields = ['firstname', 'surname', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = Customer.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
            'The email you supplied has already been used.'
            )
        return email