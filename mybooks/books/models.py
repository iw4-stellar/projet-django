from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='book_covers/')
    publisher = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
