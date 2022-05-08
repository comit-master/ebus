from django.urls import path
from shop.views import displayhome

urlpatterns = [
    path('', displayhome, name='home' ),
]
