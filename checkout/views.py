import stripe
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from decouple import config
from basket.models import BasketItem, Basket
from store.models import Product, Order, OrderItem
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

stripe.api_key = config('STRIPE_SECRET_KEY')


# Create stripe checkout session if logged in
def create_checkout_session(request, pk):
    items = []
    basket = get_object_or_404(Basket, id=pk)
    basket_items = BasketItem.objects.filter(basket=basket)
    
    for item in basket_items:
        product = get_object_or_404(Product, id=item.product.id)
        items.append(
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': str(product.name),
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': item.quantity,
            })

    checkout_session = stripe.checkout.Session.create(
        line_items=items,
        mode='payment',
        success_url=config('DOMAIN') + reverse('checkout:success'),
        cancel_url=config('DOMAIN') + reverse('checkout:cancelled'),
        metadata={'basket_id': basket.id}
    )
    return redirect(checkout_session.url, code=303)


# Create checkout session for guest checkout
def create_guest_checkout_session(request):
    items = []
    basket = request.session.get('basket', {})
    
    for product_id, quantity in basket.items():
        quantity = int(quantity)
        product = get_object_or_404(Product, id=product_id)
        items.append(
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': str(product.name),
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': quantity,
            })

    checkout_session = stripe.checkout.Session.create(
        line_items=items,
        mode='payment',
        success_url=config('DOMAIN') + reverse('checkout:success'),
        cancel_url=config('DOMAIN') + reverse('checkout:cancelled'),
    )
    return redirect(checkout_session.url, code=303)


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = config('STRIPE_WEBHOOK_SECRET')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_checkout_session(session)
    
    return HttpResponse(status=200)


def handle_checkout_session(session):
    basket_id = session.get('metadata', {}).get('basket_id')
    if not basket_id:
        return
    
    basket = get_object_or_404(Basket, id=basket_id)
    order = Order.objects.create(
        user=basket.user,
        total_amount=session['amount_total'] / 100,
        stripe_payment_intent=session['payment_intent']
    )
    
    basket_items = BasketItem.objects.filter(basket=basket)
    for item in basket_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    
    basket_items.delete()  # Clear basket items
    basket.delete()  # Delete the basket


class SuccessView(TemplateView):
    template_name = "success.html"

    def get(self, request, *args, **kwargs):
        if 'basket' in request.session:
            del request.session['basket']
        return super().get(request, *args, **kwargs)


class CancelledView(TemplateView):
    template_name = "cancel.html"
