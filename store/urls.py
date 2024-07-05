from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.StoreFront.as_view(), name='storefront'),
]
