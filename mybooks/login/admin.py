from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Bookseller


class CustomUserAdmin(UserAdmin):
    pass


# Add of 'role' filter to user model admin page
CustomUserAdmin.list_filter = CustomUserAdmin.list_filter + ("role",)

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Client)
admin.site.register(Bookseller)
