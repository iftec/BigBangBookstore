from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


# Base customer details
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    house = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


# Base product details for each book
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True,
                                   null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='uploads/products/')
    author = models.CharField(max_length=100)
    category = models.ManyToManyField('Category', related_name='products')

    def __str__(self):
        return self.name


# Base order details for each order
class Order(models.Model):
    # Define choices for updating orders
    ORDER_STATUS = {
        "Open": "Open",
        "Paid": "Paid",
        "Shipped": "Shipped",
        "Cancelled": "Cancelled",
    }
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    ship_house = models.CharField(max_length=50)
    ship_street = models.CharField(max_length=50)
    ship_address_2 = models.CharField(max_length=50, blank=True, null=True)
    ship_city = models.CharField(max_length=50)
    ship_postcode = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, default="Open",
                              choices=ORDER_STATUS),
    uuid = ShortUUIDField(max_length=4)
    reference = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.date} {self.customer}'

# Add signal to update the reference just before save
@receiver(pre_save, sender=Order)
def set_refernce(sender, instance, **kwargs):
    if not instance.reference:
        date_str = str(instance.date)
        date_ref = date_str.replace('-', '')
        instance.reference = f"{date_ref}-{instance.uuid[:4]}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.order} - {self.item}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
