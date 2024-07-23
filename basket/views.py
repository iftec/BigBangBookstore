from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, View, CreateView
from store.models import Product, Order, OrderItem
from .models import Basket, BasketItem
from .forms import AddToBasketForm
from store.forms import UserSignUpForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponse


class BasketView(ListView):
    def get(self, request, *args, **kwargs):
        update_qty_item = self.request.GET.get('item', '')
        updated_qty = self.request.GET.get('qty', '')
        if request.user.is_authenticated:
            # Get users basket or create a new one if dosen't exist
            # and flag if it's a new basket
            basket, new_basket = Basket.objects.get_or_create(
                user=request.user
                )
            basket_items = BasketItem.objects.filter(basket=basket)
            # Define variables
            items = []
            total_price = 0
            total_items = 0
            # Loop through any items in the basket
            # and get product info from database
            for item in basket_items:
                product = get_object_or_404(Product, id=item.product.id)
                line_cost = item.quantity * product.price
                if update_qty_item == str(item.id):
                    item.quantity = updated_qty
                # Add each item to the items list
                items.append({'product': product, 'quantity': item.quantity,
                              'line_cost': line_cost, 'id': item.id})
                # Update the total basket price
                total_price += total_price + line_cost
                total_items += item.quantity
            return render(request, 'basket.html',
                          {'items': items, 'total_price': total_price,
                           'item_count': total_items, 'basket': basket})
        else:
            # Get or create a session basket
            basket = request.session.get('basket', {})
            # Create an items list & set initial basket cost
            items = []
            total_price = 0
            total_items = 0
            # Loop through any items in the basket
            # and get the product info from the database
            if basket is None:
                pass
            else:
                for product_id, quantity, in basket.items():
                    product = get_object_or_404(Product, id=product_id)
                    if update_qty_item == product_id:
                        quantity = int(updated_qty)
                    # Add each item to the items list
                    items.append({'product': product, 'quantity': quantity,
                                  'line_cost': quantity * product.price,
                                  'id': product_id})
                    # Update the basket cost
                    total_price += quantity * total_price
                    total_items += quantity
            return render(request, 'basket.html',
                          {'items': items, 'total_price': total_price,
                           'item_count': total_items})


class AddToBasketView(View):
    def post(self, request, *args, **kwargs):
        # Get the selected product details from the database
        product = get_object_or_404(Product, id=kwargs['product_id'])
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            product_id = str(product.id)
            if request.user.is_authenticated:
                # Get users basket or create one if dosen't exist
                # seperate returned tuple
                user_basket, new_basket = Basket.objects.get_or_create(
                    user=request.user)
                # Check for the same exisiting items basket
                # or flag if it's a new item
                basket_item, new_item = BasketItem.objects.get_or_create(
                    basket=user_basket, product=product)
                if new_item:
                    # Add the requested quantity to the basket
                    basket_item.quantity = form.cleaned_data['quantity']
                    print(form.cleaned_data['quantity'])
                else:
                    # Or increase by the requested quantity
                    basket_item.quantity += form.cleaned_data['quantity']
                    print(form.cleaned_data['quantity'])
                # Save the updated item
                basket_item.save()
            else:
                # Get the session's basket
                basket = request.session.get('basket', {})
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
        if request.user.is_authenticated:
            # Get the item from the passed id and delete from basket
            item = get_object_or_404(BasketItem, id=kwargs['item_id'],
                                     basket__user=request.user)
            # Shorten book name for messages
            if len(item.product.name) > 30:
                item_name = item.product.name[:30] + '...'
            else:
                item_name = item.product.name

            try:
                item.delete()
                messages.success(
                    request, f'"{item_name}" was removed from your basket.')
            except BasketItem.DoesNotExist:
                messages.error(
                    request, f'"{item_name}" is not in your basket.')
        else:
            # Get the basket from the session data
            basket = request.session.get('basket', {})
            # Get the id and check if it exists and delete
            product_id = str(kwargs['item_id'])
            item = get_object_or_404(Product, id=product_id)
            item_name = item.name
            if product_id in basket:
                del basket[product_id]
                messages.success(
                    request, f'Book "{item_name}" removed from your basket.')
            else:
                messages.error(
                    request, f'Book "{item_name}" is not in your basket.')
            # Update the session basket
            request.session['basket'] = basket
        return redirect('basket:basket')


def UpdateBasket(request):
    update_qty_item = request.GET.get('item', '')
    updated_qty = request.GET.get('qty', '')
    if request.user.is_authenticated:
        item = get_object_or_404(BasketItem, id=update_qty_item,
                                 basket__user=request.user)
        item.quantity = int(updated_qty)
        item.save()
    else:
        basket = request.session['basket']
        if update_qty_item in basket:
            basket[update_qty_item] = int(updated_qty)
        request.session['basket'] = basket
    return redirect('basket:basket')  


def CreateOrder(request):
    if request.user.is_authenticated:
        # Get the customers profile
        customer_profile = request.user.customer
        # Create the customers order and add items
        order = Order.objects.create(customer=customer_profile)
        basket = get_object_or_404(Basket, user=request.user)
        basket_items = BasketItem.objects.filter(basket=basket)
        for item in basket_items:
            OrderItem.objects.create(
                order=order,
                item=item.product,
                quantity=item.quantity
            )
        # Delete the basket
        basket.delete()
        return redirect('basket:checkout-complete', order_id=order.id)
    else:
        order = Order.objects.create(customer=None)
        basket = request.session['basket']
        for product_id, quantity in basket.items():
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(
                order=order,
                item=product,
                quantity=quantity
            )
        del request.session['basket']
        return render(request, 'checkout_complete.html',
                        {'order_id': order.id,
                         'order_ref': order.reference})
