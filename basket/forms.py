from django import forms
from .models import BasketItem


class AddToBasketForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['quantity']


class IncreaseQuantityForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['quantity']
