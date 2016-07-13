from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Client(models.Model):
    
    first_name = models.CharField(verbose_name = 'First name', max_length = 50)
    last_name = models.CharField(verbose_name = 'Last name', max_length = 50)
    address = models.TextField()
    

class Producer(models.Model):
    
    first_name = models.CharField(verbose_name = 'First name', max_length = 50)
    last_name = models.CharField(verbose_name = 'Last name', max_length = 50)
    address = models.TextField()
    description = models.TextField()
    picture = models.CharField(max_length = 100)
    organic = models.BooleanField()
    

class UnitType(models.Model):
    
    name = models.CharField(max_length = 50)


class ProductType(models.Model):
    
    name = models.CharField(max_length = 50)
    description = models.TextField()
    
    
class Product(models.Model):
    
    producer = models.ForeignKey(Producer)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    product_type = models.ForeignKey(ProductType)
    quantity = models.FloatField()
    unit = models.ForeignKey(UnitType)
    price = models.FloatField()
    picture = models.CharField(max_length = 100)


class Sale(models.Model):
    
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField()
    

class ProductPerSale(models.Model):
    
    sale = models.ForeignKey(Sale)
    product = models.ForeignKey(Product)
    initial_quantity = models.IntegerField()
    available_quantity = models.IntegerField()


class Cart(models.Model):
    
    client = models.ForeignKey(Client)
    sale = models.ForeignKey(Sale)
    products = models.ManyToManyField(Product)

class Command(models.Model):
    
    client = models.ForeignKey(Client)
    sale = models.ForeignKey(Sale)
    products = models.ManyToManyField(Product)
    
    
