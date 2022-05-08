from django.urls import path
from shop.views import displayhome, detail

urlpatterns = [
    path('', displayhome, name='home' ),
    path('<int:myid>', detail, name='detail' ),
]
