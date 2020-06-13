from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("html/", views.html, name="html"),
    path("hi/<str:name>", views.hello, name="hello"),
]