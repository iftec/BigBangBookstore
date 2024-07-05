from django.db import models

import datetime


# Base customer details
class Customer(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    house = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Base product details for each book
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default='', blank=True,
                                   null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='uploads/products/')

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ship_house = models.CharField(max_length=50)
    ship_street = models.CharField(max_length=50)
    ship_address_2 = models.CharField(max_length=50, blank=True, null=True)
    ship_city = models.CharField(max_length=50)
    ship_postcode = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(max_length=10, default="Open",
                              choices=ORDER_STATUS)

    def __str__(self):
        return self.product
