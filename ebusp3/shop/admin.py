from django.contrib import admin
from .models import Product, Section, Order
# Register your models here.

class AdminSection(admin.ModelAdmin):
    list_display = ('name','date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','categorie','date_added')

class AdminOrder(admin.ModelAdmin):
    list_display = ('items', 'name','email', 'address', 'city', 'country', 'total','order_date')

admin.site.register(Product, AdminProduct)
admin.site.register(Section, AdminSection)
admin.site.register(Order, AdminOrder)