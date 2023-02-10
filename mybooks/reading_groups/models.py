from django.db import models
from users.models import Bookseller, Client

# Create your models here.


class ReadingGroup(models.Model):
    title = models.CharField(max_length=256)
    capacity = models.IntegerField()
    bookseller = models.ForeignKey(Bookseller, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
