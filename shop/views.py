from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from api.models import Product
from .models import Cart, CartItem
from authentication.models import Profile

def home(request):
    product_data = Product.objects.all()
    return render(request, "shop/products.html", {'product_data': product_data, 'query': ''})


@login_required
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.select_related('product')
    total = cart.total_price()
    return render(request, 'shop/cart.html', {
        'cart': cart,
        'items': items,
        'total': total,
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    return redirect('home')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')


@login_required
def delete_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')


def products(request):
    query = request.GET.get('q', '')
    if query:
        product_data = Product.objects.filter(title__icontains=query)
    else:
        product_data = Product.objects.all()
    return render(request, 'shop/products.html', {'product_data': product_data, 'query': query})


def search(request):
    query = request.GET.get('q', '')
    if query:
        product_data = Product.objects.filter(title__icontains=query)
    else:
        product_data = Product.objects.none()
    return render(request, 'shop/products.html', {'product_data': product_data, 'query': query})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    username = profile.user.username
    return render(request, 'auth/profile.html', {'username': username})