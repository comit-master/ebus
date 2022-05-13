import email
from unicodedata import category
from django.db import models
from django.db.models.fields.related import ForeignKey
# Create your models here.




class Section(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    #section added in first line
    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(max_length=2000)
    categorie = ForeignKey(Section, related_name='section', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title


class Order(models.Model):
    items = models.CharField(max_length=300) 
    total = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    order_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-order_date'] #order ranking, most recent

    def __str__(self):
        return self.name #display name refer to the order