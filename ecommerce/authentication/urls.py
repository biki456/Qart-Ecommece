from django.urls import path
from .views import login,logout_view,register,profile

urlpatterns = [
    path("login/",login,name="login"),
    path("logout/",logout_view,name="logout"),
    path("register/",register,name="register"),
    path("profile/",profile,name="profile"),
    
]