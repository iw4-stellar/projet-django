from functools import wraps
from django.http import HttpResponseRedirect
from .models import Bookseller


def booksellers_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        user = request.user

        if user.is_bookseller():
            bookseller = Bookseller.objects.get(user=user)

            request.bookseller = bookseller

            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")

    return wrap
