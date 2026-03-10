@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            # messages.success(request, f"Decreased quantity of {product.title}.")
        else:
            cart_item.delete()
            # messages.success(request, f"Removed {product.title} from your cart.")
    except CartItem.DoesNotExist:
        messages.warning(request, "That product was not in your cart.")

    return redirect('cart')