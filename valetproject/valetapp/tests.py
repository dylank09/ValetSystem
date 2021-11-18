from django.test import TestCase
from valetapp.forms.signup import SignUpForm

class signup_form_test(TestCase):

    def test_signup_labels(self):
        signup_form = SignUpForm()
        self.assertTrue(signup_form.fields['first_name'].label is None)
        self.assertTrue(signup_form.fields['last_name'].label is None)
        self.assertTrue(signup_form.fields['email'].label is None)

    def test_signup_success(self):
        user_data = {
            'username': 'dylank09',
            'first_name': 'Dylan',
            'last_name': 'Kearney',
            'email': 'dk@gmail.com',
            'password1': 'audi1234',
            'password2': 'audi1234',
        }
        signup_form = SignUpForm(user_data)
        self.assertTrue(signup_form.is_valid())
        user = signup_form.save()
        self.assertTrue(getattr(user, 'username'), 'dylank09')
        self.assertTrue(user.check_password('audi1234'))

    def test_signup_fail(self):
        user_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        form = SignUpForm(user_data)
        self.assertFalse(form.is_valid())

    def test_signup_password_empty(self):
        user_data = {
            'username': 'dylank123',
            'first_name': 'Dylan',
            'last_name': 'Kearney',
            'email': 'dk@mail.com',
            'password1': '',
            'password2': '',
        }
        form = SignUpForm(user_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, ['This field is required.'])
        self.assertEqual(form['password2'].errors, ['This field is required.'])
