from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomUserRegistrationForm

from django.contrib.auth.forms import UserCreationForm

def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')

                if user.is_staff:
                    return redirect('main_view') 
                else:
                    return redirect('home') 
            else:
                messages.error(request, 'error')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Store") 
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')