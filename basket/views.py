from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, View
from store.models import Product
from .forms import AddToBasketForm


class BasketView(ListView):
    def get(self, request, *args, **kwargs):
        # Get the sessions basket, will create if dosen't exisit
        basket = request.session.get('basket', {})
        # Create an items dictionary
        items = []
        total_price = 0
        # For any items already in the items dictionary
        # loop through and get from database
        for product_id, quantity, in basket.items():
            product = get_object_or_404(Product, id=product_id)
            items.append({'product': product, 'quantity': quantity,
                          'total_price': quantity * product.price})
            total_price += quantity * total_price
        return render(request, 'basket.html',
                      {'items': items, 'total_price': total_price})


class AddToBasketView(View):
    def post(self, request, *args, **kwargs):
        # Get the selected product details from the database
        product = get_object_or_404(Product, id=kwargs['product_id'])
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            # Get the session's basket
            basket = request.session.get('basket', {})
            product_id = str(product.id)
            # If item isn't in basket already, add it to the basket,
            # otherwise add to the existing quantity
            if product_id in basket:
                basket[product_id] += form.cleaned_data['quantity']
            else:
                basket[product_id] = form.cleaned_data['quantity']
            request.session['basket'] = basket
        return redirect('basket:basket')


class RemoveFromBasketView(View):
    def post(self, request, *args, **kwargs):
        # Get the session's basket
        basket = request.session.get('basket', {})
        # Get the selected products id
        product_id = str(kwargs['product_id'])
        # Delete it from the basket
        if product_id in basket:
            del basket[product_id]
        # Update the session's basket
        request.session['basket'] = basket
        return redirect('basket:basket')
