from django.db import models
from bookseller.models import Bookseller

# Create your models here.


class ReadingGroup(models.Model):
    bookseller = models.ForeignKey(Bookseller, on_delete=models.CASCADE)

    title = models.CharField(max_length=256)
    capacity = models.IntegerField()
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.title
