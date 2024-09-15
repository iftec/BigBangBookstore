from django.urls import path
from . import views
from basket.views import CreateOrder

app_name = "checkout"

urlpatterns = [
    path('<int:pk>/', views.create_checkout_session, name='checkout'),
    path('', views.create_guest_checkout_session, name="guest-checkout"),
    path('<int:order_id>/success/', views.success_view, name="success"),
    path('<int:order_id>/cancel/', views.cancelled_view, name="cancelled"),
    path('stripe_webhook/', views.stripe_webhook, name="stripe-webhook"),
]

