from django.urls import path
from . import views

urlpatterns = [
    path("html-form/", views.html_form, name="html-form"),
    path("django-form/", views.django_form, name="django-form")
]