from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from store.models import Customer  # Import Customer model


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    order_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('name', '').strip()

        if full_name:
            split_name = full_name.split(' ', 1)
            self.cleaned_data['first_name'] = split_name[0]
            self.cleaned_data['last_name'] = split_name[1] if len(
                split_name) > 1 else ''

        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        # Set the username to the email address
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

# added for update address


class AddressUpdateForm(forms.ModelForm):
    # Create a custom field for email not directly tied to the Customer model
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'style': 'background-color: #D8C2E3;'}),
        label='Email Address'
    )

    class Meta:
        model = Customer
        fields = ['email', 'phone', 'street', 'address_2', 'city', 'postcode']
        widgets = {
            'street': forms.TextInput(
                attrs={'style': 'background-color: #D8C2E3;'}),
            'address_2': forms.TextInput(
                attrs={'style': 'background-color: #D8C2E3;'}), 
            'city': forms.TextInput(
                attrs={'style': 'background-color: #D8C2E3;'}),
            'postcode': forms.TextInput(
                attrs={'style': 'background-color: #D8C2E3;'}),
            'phone': forms.TextInput(
                attrs={'style': 'background-color: #D8C2E3;'}),
            'email': forms.TextInput(
                attrs={'style': 'background-color: #D8C2E3;'}),
        }
        labels = {
            'street': 'House & Street',
            'address_2': 'Address Line 2',
            'phone': 'Phone Number',
        }

    def __init__(self, *args, **kwargs):
        # Accept user instance as a keyword argument
        user = kwargs.pop('user', None)

        super(AddressUpdateForm, self).__init__(*args, **kwargs)
        # Set all fields to not be required
        for field in self.fields.values():
            field.required = False

        # Set initial value of email field if user is provided
        if user:
            self.fields['email'].initial = user.email
