from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout

from django.contrib.auth.views import LoginView

class CustomLogin(LoginView):
    template_name = 'auth/login.html'

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
        
        else:
            form = RegisterForm()

    form = RegisterForm
    context = {'form':form}
    return render(request,"auth/register.html",context)

def profile(request):
    
    user = request.user
    profile = user.profile
    context = {'user':user,'profile':profile}
    return render(request,"auth/profile.html",context)

