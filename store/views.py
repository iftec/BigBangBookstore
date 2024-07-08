from django.shortcuts import render
from django.views import generic
from .models import Product


class StoreFront(generic.ListView):
    template_name = "storefront.html"
    queryset = Product.objects.all().order_by('name')
    context_object_name = "products"
    paginate_by = 12


class ProductDetails(generic.DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"
