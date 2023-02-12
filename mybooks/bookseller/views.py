from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import booksellers_only


# Create your views here.
@login_required
@booksellers_only
def indexView(request):
    template = "bookseller/index.html"
    return render(request, template)
