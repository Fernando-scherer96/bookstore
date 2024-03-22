from django.db import models
from .category import Category

class Product(models.Model):
    title = models. CharField(max_length = 100)
    description = models.TextField(max_length = 500, blank = True, null = False)
    price = models.PositiveIntegerField(null = True)
    #frague para dizer se o produto está ativo ou não
    active = models.BooleanField(default = True)
    #manytomany = muitos para muitos
    categorie = models.ManyToManyField(Category, blank=True)

