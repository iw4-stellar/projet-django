from django.db import models

# Import the models from the other apps

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to="book_covers/")
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
