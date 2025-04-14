"""Django views"""
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def index(request):
    return render(request, "index.html")

def login(request):
    """Login page view"""
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def register(request):
    """Register page view"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

