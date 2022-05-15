from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=80, db_index=True)


class Label(models.Model):
    name = models.CharField(max_length=200, db_index=True)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    brand = models.ForeignKey(Brand, related_name='brand', on_delete=models.CASCADE,
                              blank=True, null=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE,
                                 blank=True, null=True)
    label = models.ManyToManyField(Label)
