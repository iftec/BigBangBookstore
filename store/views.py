from django.views import generic
from .models import Product, Category, Customer, Order
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm, UserSignUpForm, AddressUpdateForm
from django.db.models import Q
from basket.forms import AddToBasketForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# StoreFront view
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


# ProductDetails view
class ProductDetails(generic.DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddToBasketForm()
        return context


# AccountLogin view
class AccountLogin(LoginView):
    template_name = "login.html"
    form = UserLoginForm


# AccountRegister view
class AccountRegister(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'signup.html'

    # Set order id to none if there isn't one
    def get(self, request, order_id=None):
        # Check if user is authenticated
        if request.user.is_authenticated:
            return redirect('/')
        else:
            # Get form and pass in order id
            form = self.form_class(initial={'order_id': order_id})
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        # Just used for checking validations errors, will remove
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            # Save the user account and create a customer profile
            user = form.save()
            customer = Customer.objects.create(
                user=user,
            )

            # Get the order id form the form
            order_id_value = form['order_id'].value()
            # Check it exists and is a number
            if order_id_value and order_id_value.isdigit():
                # Grab the corresponding order
                order = get_object_or_404(
                    Order, id=form.cleaned_data['order_id'])
                # Attached the customer to the order
                order.customer = customer
                order.status = "Paid"
                order.save()
            # If there's no order just skip
            else:
                pass
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request, 'There was an issue registering. Please try again')
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse("store:login")


# AccountLogOut view
def AccountLogOut(request):
    logout(request)
    return redirect('/')

# New account_page view for managing user account
@login_required
def account_page(request):
    # Ensure password_form is always defined
    password_form = PasswordChangeForm(request.user)
    # Initialize address form with current customer data
    address_form = AddressUpdateForm(user=request.user, instance=request.user.customer)


    if request.method == 'POST':
        if 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                # Log out the user after password change
                logout(request)
                messages.success(request, 'Your password was successfully updated! Please log in again.')
                return redirect('login')
            else:
                messages.error(request, 'The password you entered is incorrect.')
        elif 'update_address' in request.POST:
            address_form = AddressUpdateForm(request.POST, user=request.user, instance=request.user.customer)
            if address_form.is_valid():
                address_form.save()
                messages.success(request, 'Your details were successfully updated.')
                # return redirect('account_page')           
            else:
                messages.error(request, 'Please correct the error below.')
        elif 'delete_account' in request.POST:
            request.user.delete()
            messages.success(request, 'Your account was successfully deleted.')
            return redirect('home')
        
    if request.method == 'GET':
        user = request.user
        orders = Order.objects.filter(customer=user.customer)

        return render(request, 'account.html', {
            'password_form': password_form,
            'address_form': address_form,
            'orders': orders,
        })

    return render(request, 'account.html', {
        'password_form': password_form,
        'address_form': address_form,
    })

