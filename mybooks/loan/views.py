from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def loanView(request):
    if request.user.is_client():
        template = "client/loans.html"
    if request.user.is_admin():
        template = "bookseller/loans.html"

    context = {}

    return render(request, template, context)
