from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField()
    email = forms.EmailField()
    house = forms.CharField()
    street = forms.CharField()
    address_2 = forms.CharField(required=False)
    city = forms.CharField()
    postcode = forms.CharField()
    order_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
