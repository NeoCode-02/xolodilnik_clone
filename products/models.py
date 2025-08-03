from django.db import models

from common.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
