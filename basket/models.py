from django.conf import settings
from django.db import models
from store.models import Product


# Basket model
class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket of {self.user.username}"


# Items attached to basket
class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='items',
                               on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.product.price
