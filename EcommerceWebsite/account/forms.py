from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Please add a valid email address')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class SignInForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Wrong email or password")