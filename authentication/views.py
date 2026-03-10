from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm,CustomPasswordChangeForm
from .models import Profile 
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        if not u or not p:
            messages.error(request, 'Please provide both username and password.')
            return render(request, 'auth/login.html')
        
        user = authenticate(request, username=u, password=p)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'auth/login.html')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            auth_login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully update')
            return redirect('profile')
        else:
            messages.error(request, 'please correct the erroe below.')

    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'auth/pass_change.html',{
        'form': form
    })

