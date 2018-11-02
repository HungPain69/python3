from django.contrib import admin
from .models import Products,Categories, Customers, Order, OrderItem, Admins, Logins, DeliveryAddresses
# Register your models here.

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Customers)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Admins)
admin.site.register(DeliveryAddresses)
admin.site.register(Logins)