from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.


def indexView(request):
    template = "books/index.html"

    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(request, template, context)


def bookView(request, id):
    template = "books/book.html"

    book = Book.objects.filter(id=id).first()

    context = {
        "book": book,
    }

    return render(request, template, context)


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("books_list")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})
