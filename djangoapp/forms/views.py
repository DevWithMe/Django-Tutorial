from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Your name:")

# Create your views here.
def html_form(request):
    if request.method == "POST":
        return HttpResponse(request.POST["name"])
    return render(request, "forms/html-form.html")

def django_form(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data["name"])

    return render(request, "forms/django-form.html", {
        "form": NameForm()
    })