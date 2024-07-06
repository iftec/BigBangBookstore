from django.shortcuts import render
from django.views import generic
from .models import Product


class StoreFront(generic.ListView):
    template_name = "storefront.html"
    queryset = Product.objects.all()
    context_object_name = "products"
