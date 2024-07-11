from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "store"

urlpatterns = [
    path('', views.StoreFront.as_view(), name='storefront'),
    path('books/<int:pk>', views.ProductDetails.as_view(),
         name='product-detail'),
    path('login/', views.AccountLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
