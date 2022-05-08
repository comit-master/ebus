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