from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from client.decorators import clients_only
from bookseller.models import Bookseller
from loan.models import InventoryItem, Loan
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

    bookItems = InventoryItem.objects.filter(book=book, quantity__gt=0)

    context = {
        "book": book,
        "bookItems": bookItems,
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


@login_required
@clients_only
def loanView(request, inventory_item_id):
    client = request.client
    item = InventoryItem.objects.filter(id=inventory_item_id).first()

    loan = Loan.objects.create(
        client=client,
        item=item,
    )

    return render("/client")
