from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=255, label="First Name")
    last_name = forms.CharField(max_length=255, label="Last Name")
    email = forms.EmailField(label="Email")
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/index.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("invalid credentials")
        else:
            return HttpResponse("Form not valid")
    else:
        return render(request, "users/login.html", {
            "form": LoginForm()
        })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            return HttpResponse("Form is not valid")
    else:
        return render(request, "users/register.html", {
            "form": RegisterForm()
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))