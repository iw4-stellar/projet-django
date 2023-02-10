from django.shortcuts import render, redirect
from .forms import BookForm

# Create your views here.

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
