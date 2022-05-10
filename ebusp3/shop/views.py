from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.



def displayhome(request):
    product_object = Product.objects.all() #retrieve all object from db
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None: # item-name is the object from index.html
        product_object = Product.objects.filter(title__icontains=item_name) #when user is writing if in db in title
        # 1 caracter of what the user is writing, display only the product 
        # title__icontains similar to like sql fct
    paginator = Paginator(product_object, 4) # show me only 4 products by page
    page = request.GET.get('page') # display the page index number 
    product_object = paginator.get_page(page) # get the page refer to the index number
    return render(request, 'shop/index.html', {'product_object': product_object})


def detail(request, myid):
    product_object = Product.objects.get(id=myid) #retrieve ID from product
    return render(request, 'shop/detail.html', {'product':product_object}) #display detail page from selected id product


def checkout(request):
    return render(request, 'shop/checkout.html')