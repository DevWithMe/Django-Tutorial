from django.urls import path

from . import views

urlpatterns = [
    path("html-form/", views.html_form, name="htmlform"),
    path("django-form/", views.django_form, name="djangoform")
]