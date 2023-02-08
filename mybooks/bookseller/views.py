from django.shortcuts import render, redirect
from users.models import User, Bookseller


# Create your views here.
def indexView(request):
    if not request.user.is_authenticated and request.user.role != Bookseller.base_role:
        return redirect("/login")

    template = "bookseller/index.html"
    return render(request, template)
