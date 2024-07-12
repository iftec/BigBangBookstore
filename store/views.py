from django.views import generic
from .models import Product, Category
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm, UserSignUpForm
from django.db.models import Q
from basket.forms import AddToBasketForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserLoginForm


class StoreFront(generic.ListView):
    template_name = "storefront.html"
    context_object_name = "products"
    paginate_by = 15

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
        context['form'] = AddToBasketForm()
        context['login_form'] = UserLoginForm()

        return context


class ProductDetails(generic.DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddToBasketForm()
        return context


class AccountLogin(LoginView):
    template_name = "login.html"
    form = UserLoginForm


class AccountRegister(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registration successful. You can now log in.')
            return redirect(self.get_success_url())
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse("store:login")


def AccountLogOut(request):
    logout(request)
    return redirect('/')