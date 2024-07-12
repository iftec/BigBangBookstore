from django.urls import path
from . import views

app_name = "basket"

urlpatterns = [
    path('', views.BasketView.as_view(), name='basket'),
    path('add/<int:product_id>/', views.AddToBasketView.as_view(),
         name='add-to-basket'),
    path('remove/<int:item_id>/', views.RemoveFromBasketView.as_view(),
         name='remove-from-basket'),
]
