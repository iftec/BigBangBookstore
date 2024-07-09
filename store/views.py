from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from django.db.models import Q


class StoreFront(generic.ListView):
    template_name = "storefront.html"
    context_object_name = "products"
    paginate_by = 12

    # Define search function
    def get_queryset(self):
        queryset = Product.objects.all().order_by('name')
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) |
                                       Q(author__icontains=search_query))
        return queryset


class ProductDetails(generic.DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"


class AccountLogin(LoginView):
    template_name = "login.html"
    form = UserLoginForm
