from django.urls import path
from .views import cart,products,search

urlpatterns = [
    path('',products,name='products'),
    path('cart/',cart,name='cart'),
    path('search/',search,name='search'),
]