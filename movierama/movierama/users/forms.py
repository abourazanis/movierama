from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs['class'] = 'invisible'
        self.fields["email"].label = ''

    def clean_email(self):
        if not self.errors:
            email = self.cleaned_data['username']
            return email
        return

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['username']
        user.save()

        return user
