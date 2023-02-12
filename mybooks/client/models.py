from django.db import models
from users.models import User

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        if self.name is not None:
            return self.name
        return super().__str__()
