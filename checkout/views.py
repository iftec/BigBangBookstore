import stripe
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from decouple import config
from basket.models import BasketItem, Basket
from store.models import Product

stripe.api_key = config('STRIPE_SECRET_KEY')


# Create stripe checkout session if logged in
def create_checkout_session(request, pk):
    # Create an items list
    items = []
    # Get all items from the basket
    basket = get_object_or_404(Basket, id=pk)
    basket_items = BasketItem.objects.filter(basket=basket)
    # Put all items in the list and structure for stripe
    for item in basket_items:
        product = get_object_or_404(Product, id=item.product.id)
        items.append(
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': item.product,
                        },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': item.quantity,
            })
    # Create strip checkout session
    checkout_session = stripe.checkout.Session.create(
        # Add the items
        line_items=items,
        mode='payment',
        # Set the success or cancel urls
        success_url=config('DOMAIN') + '/checkout/success/',
        cancel_url=config('DOMAIN') + '/checkout/cancel/',
    )
    return redirect(checkout_session.url, code=303)


# Create checkout session for guest checkout
def create_guest_checkout_session(request):
    # Create item list
    items = []
    # Get basket
    basket = request.session['basket']
    for product_id, quantity in basket:
        quantity = int(quantity)
        product = get_object_or_404(Product, id=product_id)
        # Add each item to the items list
        items.append(
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': product,
                        },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': quantity,
            }),
    # Create strip checkout session
    checkout_session = stripe.checkout.Session.create(
        # Add the items
        line_items=items,
        mode='payment',
        # Set the success or cancel urls
        success_url=config('DOMAIN') + '/checkout/success/',
        cancel_url=config('DOMAIN') + '/checkout/cancel/',
    )
    return redirect(checkout_session.url, code=303)


# Checkout success view
class SuccessView(TemplateView):
    template_name = "success.html"


# Checkout cancelled view
class CancelledView(TemplateView):
    template_name = "cancel.html"