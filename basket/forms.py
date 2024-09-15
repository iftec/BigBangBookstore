from django import forms
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm
from .models import BasketItem  # Import BasketItem from the current module
from store.models import Customer  # Import Customer from the store module

# Form to add items to the basket
class AddToBasketForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['quantity']  # Only the quantity field is needed for adding to the basket

# Form to increase the quantity of items in the basket
class IncreaseQuantityForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['quantity']  # Only the quantity field is needed for increasing the quantity

# Form to change the user's password
class PasswordChangeForm(AuthPasswordChangeForm):
    pass  # Inherits all functionality from the built-in PasswordChangeForm

