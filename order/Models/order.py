from django.db import models
from django.contrib.auth.models import User
from product.Models.product import Product


class Order(models.Model):
    product = models.ManyToManyField(Product, blank = False)
    User = models.ForeignKey(User, on_delete = models.CASCADE ,null = False)