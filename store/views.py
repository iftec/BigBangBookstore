from django.shortcuts import render
from django.views import generic
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView


class StoreFront(generic.ListView):
    template_name = "storefront.html"
    queryset = Product.objects.all().order_by('name')
    context_object_name = "products"
    paginate_by = 12


class ProductDetails(generic.DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"


class AccountLogin(LoginView):
    template_name = "login.html"
