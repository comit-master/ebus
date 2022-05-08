from django.shortcuts import render

# Create your views here.



def displayhome(request):
    return render(request, 'shop/index.html')