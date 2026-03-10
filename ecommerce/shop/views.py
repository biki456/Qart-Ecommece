from django.shortcuts import render


def products(request):
    return render(request,"shop/products.html")

def cart(request):
    return render(request,"shop/cart.html")

def search(request):
    return render(request,"shop/search.html")

