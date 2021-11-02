from django.forms import ModelForm
from django import forms
from ..models.users.customer import Customer
from django.contrib.auth import authenticate

class LoginForm(ModelForm):
    email = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput,  min_length=8, max_length=12, required=True)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This user is no active')
        return super(LoginForm, self).clean(*args, **kwargs)

    class Meta:
        model = Customer
        fields = ['email', 'password']
