from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def hello(request, name):
    return HttpResponse(f"Hello {name}")

def html(request):
    return render(
        request, "firstapp/index.html"
    )