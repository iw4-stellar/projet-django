from django.db import models
# Import the models from the other apps

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.OneToOneField('Author', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='book_covers/')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Collection(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)

