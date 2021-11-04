from django.test import TestCase
from valetapp.forms.signup import SignUpForm

class SignUpForm_Test(TestCase):

    def test_signup_labels(self):
        signupForm = SignUpForm()
        self.assertTrue(signupForm.fields['first_name'].label is None)
        self.assertTrue(signupForm.fields['last_name'].label is None)
        self.assertTrue(signupForm.fields['email'].label is None)

    def test_signup_success(self):
        userData = {
            'username': 'dylank09',
            'first_name': 'Dylan',
            'last_name': 'Kearney',
            'email': 'dk@gmail.com',
            'password1': 'audi1234',
            'password2': 'audi1234',
        }
        signupForm = SignUpForm(userData)
        self.assertTrue(signupForm.is_valid())
        user = signupForm.save()
        self.assertTrue(getattr(user, 'username'), 'dylank09')
        self.assertTrue(user.check_password('audi1234'))

    def test_signup_fail(self):
        userData = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        form = SignUpForm(userData)
        self.assertFalse(form.is_valid())

    def test_signup_password_empty(self):
        userData = {
            'username': 'dylank123',
            'first_name': 'Dylan',
            'last_name': 'Kearney',
            'email': 'dk@mail.com',
            'password1': '',
            'password2': '',
        }
        form = SignUpForm(userData)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, ['This field is required.'])
        self.assertEqual(form['password2'].errors, ['This field is required.'])
