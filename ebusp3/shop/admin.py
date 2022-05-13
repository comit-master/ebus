from django.contrib import admin
from .models import Product, Section, Order
# Register your models here.

class AdminSection(admin.ModelAdmin):
    list_display = ('name','date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','categorie','date_added')

admin.site.register(Product, AdminProduct)
admin.site.register(Section, AdminSection)
admin.site.register(Order)