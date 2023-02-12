from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Type(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        BOOKSELLER = "BOOKSELLER", "Bookseller"
        CLIENT = "CLIENT", "Client"

    user_type = models.CharField(
        max_length=16, choices=Type.choices, default=Type.ADMIN
    )

    def is_admin(self):
        return self.user_type == User.Type.ADMIN

    def is_bookseller(self):
        return self.user_type == User.Type.BOOKSELLER

    def is_client(self):
        return self.user_type == User.Type.CLIENT
