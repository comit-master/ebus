from django.contrib import admin
from .models import Product, Section, Order
# Register your models here.

admin.site.site_header = "ShopFire Administration"
admin.site.site_title = "SF Shop"
admin.site.index_title = "Management"

class AdminSection(admin.ModelAdmin):
    list_display = ('name','date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','categorie','date_added')
    search_fields = ('title',)
    list_editable = ('price',)
class AdminOrder(admin.ModelAdmin):
    list_display = ('items', 'name','email', 'address', 'city', 'country', 'total','order_date')

admin.site.register(Product, AdminProduct)
admin.site.register(Section, AdminSection)
admin.site.register(Order, AdminOrder)