from django.contrib import admin
from .models import Bookseller, Client, User

# Register your models here.
admin.site.register(User)
admin.site.register(Bookseller)
admin.site.register(Client)