from django import forms
from .models import Book, Author, Publisher, Collection, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'publisher', 'collection', 'genre']
