from django.shortcuts import render
from .models import Product

# Create your views here.



def displayhome(request):
    product_object = Product.objects.all() #retrieve all object from db
    return render(request, 'shop/index.html', {'product_object': product_object})