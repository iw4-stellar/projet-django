from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        BOOKSELLER = "BOOKSELLER", "Bookseller"
        CLIENT = "CLIENT", "Client"

    base_role = Role.ADMIN

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=32, choices=Role.choices, default=Role.ADMIN)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


# Client related models
class Client(User):
    base_role = User.Role.CLIENT

    class Meta:
        proxy = True


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Client)
def create_client_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.CLIENT.value:
        ClientProfile.objects.create(user=instance)


# Bookseller related models
class Bookseller(User):
    base_role = User.Role.BOOKSELLER

    class Meta:
        proxy = True


class BooksellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bookseller_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Bookseller)
def create_bookseller_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.BOOKSELLER.value:
        BooksellerProfile.objects.create(user=instance)
