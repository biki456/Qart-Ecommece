from django.urls import path
from .views import pay
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pay', pay, name='pay')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR)
