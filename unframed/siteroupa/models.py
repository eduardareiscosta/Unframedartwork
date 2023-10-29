from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
CATEGORY_CHOICES = (
    ('C', 'Clothes'),
    ('A', 'Accessories')
)

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=150, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default = 1)
    description = models.CharField(max_length=250, default='', blank=True)
    color = models.CharField(max_length=30, blank=True)
    stock = models.IntegerField(default=0)
    onsale = models.BooleanField(default=False)
    pub_data = models.DateTimeField(default=timezone.now())
    main_image = models.ImageField(null=True, blank=True)
    #falta imagem

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default = 0) #item * quantity
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(default=False)

    def total_price(self):
        return self.item.price * self.quantity

class ItemImage(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/siteroupa/images/')


