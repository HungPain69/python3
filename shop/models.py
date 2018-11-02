
from django.db import models

# Create your models here.i


class Customers(models.Model):
    forename = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    add1 = models.CharField(max_length=200)
    add2 = models.CharField(max_length=200)
    add3 = models.CharField(max_length=200)
    phone = models.CharField(max_length=14, blank=True)
    email = models.EmailField()
    postcode = models.IntegerField(default=0)
    registered = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.forename


class Logins(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.username



class DeliveryAddresses (models.Model):
    forename = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    add1 = models.CharField(max_length=200)
    add2 = models.CharField(max_length=200)
    add3 = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    postcode = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.forename


class Order(models.Model):
    customer_id= models.ForeignKey(Customers, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    delivery_add_id= models.ForeignKey(DeliveryAddresses, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    date = models.DateTimeField()
    status = models.CharField(max_length=50)
    session = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.status

class Categories(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Products(models.Model):
    cat_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    price = models.FloatField()
    objects = models.Manager()

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.Case)
    quanlity = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.quanlity







class Admins(models.Model):
    username = models.CharField(max_length =50)
    password = models.CharField(max_length =50)
    objects = models.Manager()

    def __str__(self):
        return self.username
    