from django.contrib import admin
from .models import Author, Collection, Publisher, Book, Genre

# Register your models here.
admin.site.register(Author)
admin.site.register(Collection)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Book)
