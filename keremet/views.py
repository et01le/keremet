"""Django views"""
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, TermForm
from .models import Term
import random

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

def study(request):
    count = Term.objects.count()
    random_index = random.randint(0, count - 1)
    term = Term.objects.all()[random_index]
    return render(request, "study.html", context = {"random_term": term})

@login_required
def contribute(request):
    """Contirbute a term"""
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            term = form.save(commit = False)
            term.created_by = request.user
            term.save()
            return redirect("index")
    else:
        form = TermForm()
    return render(request, "contribute.html", {"form": form})

def all(request):
    terms = Term.objects.all()
    return render(request, "all.html", context = {"terms": terms})

