from django.db import models

from eshop.accounts.models import Suplier, Customer

class Category (models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

class Product (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    pictures = models.ImageField
    price = models.IntegerField()
    discount = models.IntegerField
    supplier = models.ForeignKey(Suplier, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="category not choosen")

class Order (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    customet_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    ship_date = models.DateField()
    total_price = models.IntegerField