from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, cart, products, profile, add_to_cart, remove_from_cart, delete_cart_item, search

urlpatterns = [
    path("", products, name="home"),
    path("cart/", cart, name="cart"),
    path("cart/add/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>", remove_from_cart, name="remove_from_cart"),
    path('cart/delete/<int:product_id>/', delete_cart_item, name='delete_cart_item'),
    path("products/", products, name="products"),
        path("search/", products, name="search"),
    path('profile/', profile, name='profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)