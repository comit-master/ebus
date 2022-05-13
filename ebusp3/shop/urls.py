from django.urls import path
from shop.views import displayhome, detail, checkout, confirm

urlpatterns = [
    path('', displayhome, name='home' ),
    path('<int:myid>', detail, name='detail' ),
    path('checkout', checkout, name='checkout' ),
    path('confirm', confirm, name='confirm' ),


]
