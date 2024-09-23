import stripe
from django.shortcuts import get_object_or_404, redirect, reverse, render
from decouple import config
from basket.models import BasketItem, Basket
from store.models import Product, Order, OrderItem
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib import messages

stripe.api_key = config('STRIPE_SECRET_KEY')


# Create checkout session for registered customer
def create_checkout_session(request, pk):
    # Set empty item dictionary for passing to stripe
    items = []
    # Set initial zero order amount
    order_amount = 0
    # Get basket from database
    basket = get_object_or_404(Basket, id=pk)
    basket_items = BasketItem.objects.filter(basket=basket)
    # Create initial order and add customer
    order = Order.objects.create(
        customer=basket.user.customer,
        status="Open",
    )
    # Loop through the basket to set out the data in correct formats
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

        # Also create the order items ready for adding to the order
        OrderItem.objects.create(
            order=order,
            item=product,
            quantity=item.quantity,
            price=product.price
        )
        # Calculate the order amount while in the for loop
        line_amount = product.price * item.quantity
        order_amount = order_amount + line_amount
    # Update and save the final order amount
    order.order_amount = order_amount
    order.save()
    # Create the checkout session
    checkout_session = stripe.checkout.Session.create(
        shipping_address_collection={"allowed_countries": ["GB"]},
        phone_number_collection={"enabled": True},
        line_items=items,
        mode='payment',
        # Pass the order id in the metadata
        metadata={'order_id': order.id, 'basket_id': basket.id},
        success_url=config('DOMAIN') + reverse('checkout:success',
                                               kwargs={'order_id': order.id}),
        cancel_url=config('DOMAIN') + reverse('checkout:cancelled',
                                              kwargs={'order_id': order.id}),
    )
    return redirect(checkout_session.url, code=303)


# Create checkout session for guest checkout
def create_guest_checkout_session(request):
    # Set empty item dictionary for passing to stripe
    items = []
    # Set initial zero order amount
    order_amount = 0
    # Get basket from session data
    basket = request.session.get('basket', {})
    # Create initail order
    order = Order.objects.create(
        status="Open",
    )
    # Loop through the basket to set out the data in correct formats
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
        # Also create the order items ready for adding to the order
        OrderItem.objects.create(
                order=order,
                item=product,
                quantity=quantity,
                price=product.price
            )
        # Calculate the order amount while in the for loop
        line_amount = product.price * quantity
        order_amount = order_amount + line_amount
    # Update and save the final order amount
    order.order_amount = order_amount
    order.save()
    # Create the checkout session
    checkout_session = stripe.checkout.Session.create(
        shipping_address_collection={"allowed_countries": ["GB"]},
        phone_number_collection={"enabled": True},
        line_items=items,
        mode='payment',
        # Pass the order id in the metadata
        metadata={'order_id': order.id},
        success_url=config('DOMAIN') + reverse('checkout:success',
                                               kwargs={'order_id': order.id}),
        cancel_url=config('DOMAIN') + reverse('checkout:cancelled',
                                              kwargs={'order_id': order.id}),
    )
    return redirect(checkout_session.url, code=303)


@csrf_exempt
@require_POST
def stripe_webhook(request):
    # Get the payload from stripe
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = config('STRIPE_WEBHOOK_SECRET')
    # Create the event with all the data
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Check the checkout was a success
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Extract shipping address details from the payload
        shipping = session.get('shipping_details', {})
        customer_phone = session.get('customer_details',
                                     {}).get('phone', 'Phone number not given')
        shipping_address = shipping.get('address', {})
        shipping_line1 = shipping_address.get('line1',
                                              'Line 1 address not supplied')
        shipping_line2 = shipping_address.get('line2')
        shipping_city = shipping_address.get('city',
                                             'City not supplied')
        shipping_postcode = shipping_address.get('postal_code',
                                                 'Post code not supplied')
        shipping_name = shipping.get('name', 'Name not given')

        stripe_payment_intent = session['payment_intent']

        # Extract the total amount
        total_amount = session.get('amount_total', 0)
        total_amount = total_amount / 100

        # Get order id and update
        order_id = session.get('metadata', {}).get('order_id', '')
        order = get_object_or_404(Order, id=order_id)
        order.status = "Paid"
        order.ship_street = shipping_line1
        order.ship_address_2 = shipping_line2
        order.ship_city = shipping_city
        order.ship_postcode = shipping_postcode
        order.reference = stripe_payment_intent
        order.ship_phone = customer_phone
        order.ship_name = shipping_name
        order.save()
        # Get basket from metadata or set as false
        basket_id = session.get('metadata', {}).get('basket_id', False)
        # Check if there is a basket and delete
        if basket_id is not False:
            basket = get_object_or_404(Basket, id=basket_id)
            basket.delete()
            print('Deleted basket!')

    return HttpResponse(status=200)


def success_view(request, order_id):
    # Delete the basket from the session data if it exists
    request.session.pop('basket', None)
    # Grab the order details
    order = get_object_or_404(Order, id=order_id)
    order_address = f"{order.ship_street} {order.ship_city} {
                                        order.ship_postcode}"
    order_items = OrderItem.objects.filter(order_id=order.id)
    order_details = {
        'order_id': order.id,
        'order_amount': order.order_amount,
        'order_name': order.ship_name,
        'order_address': order_address,
        'order_reference': order.reference,
        }
    # Build the context
    context = {
        'order_items': order_items,
        'order_details': order_details
    }
    # Send it to the success page
    return render(request, 'success.html', context)


def cancelled_view(request, order_id):
    # Get the order and delete it
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    # Set the message notifying the order was cancelled
    messages.info(request, "Your order was cancelled. \
                  Please contact us if you are having issues.")
    # Redirect back to the basket
    return redirect(reverse('basket:basket'))
