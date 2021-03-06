from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
