from django.contrib import admin
from .models import ReadingGroup

class ReadingGroupAdmin(admin.ModelAdmin):
  list_display = ('title', 'bookseller')

# Register your models here.
admin.site.register(ReadingGroup, ReadingGroupAdmin)