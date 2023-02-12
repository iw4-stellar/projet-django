from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import clients_only


# Create your views here.
@login_required
@clients_only
def indexView(request):
    template = "client/index.html"
    return render(request, template)
