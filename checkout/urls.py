from django.urls import path
from . import views

app_name = "checkout"

urlpatterns = [
     path('<int:pk>/', views.create_checkout_session, name='checkout'),
     path('', views.create_guest_checkout_session, name="guest-checkout"),
     path('success/', views.SuccessView.as_view(), name="success"),
     path('cancel/', views.CancelledView.as_view(), name="cancelled"),
]
