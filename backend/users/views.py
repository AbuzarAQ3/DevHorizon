from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('signup')
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('homepage')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('homepage')