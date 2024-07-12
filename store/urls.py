from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.StoreFront.as_view(), name='storefront'),
    path('books/<int:pk>', views.ProductDetails.as_view(),
         name='product-detail'),
    path('login/', views.AccountLogin.as_view(), name='login'),
    path('logout/', views.AccountLogOut, name='logout'),
    path('register/', views.AccountRegister.as_view(), name='signup'),
]
