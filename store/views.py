from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Product, Category
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
        price_filter = self.request.GET.get('price', '')
        author_filter = self.request.GET.get('author', '')
        category_filter = self.request.GET.get('category', '')

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) |
                                       Q(author__icontains=search_query))

        if price_filter:
            if price_filter == 'desc':
                queryset = queryset.order_by('-price')
            elif price_filter == 'asec':
                queryset = queryset.order_by('price')
            elif price_filter == 'under10':
                queryset = queryset.order_by('price').filter(price__lt=10.00)
            elif price_filter == 'under5':
                queryset = queryset.order_by('price').filter(price__lt=5.00)

        if author_filter:
            queryset = queryset.filter(author__icontains=author_filter)

        if category_filter:
            queryset = queryset.filter(
                category__name__icontains=category_filter
                )

        return queryset

    # Build context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get a unique list of authors
        authors_list = Product.objects.values_list(
            'author', flat=True).distinct()
        # Pass author list to context
        context['authors_list'] = authors_list.order_by('author')
        # Get list of categories and pass them into the context
        context['categories'] = Category.objects.all().order_by('name')
        # Pass in the url parameters into the context
        context['category_filter'] = self.request.GET.get('category', '')
        context['author_filter'] = self.request.GET.get('author', '')
        context['price_filter'] = self.request.GET.get('price', '')

        return context


class ProductDetails(generic.DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"


class AccountLogin(LoginView):
    template_name = "login.html"
    form = UserLoginForm
