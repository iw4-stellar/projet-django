from functools import wraps
from django.http import HttpResponseRedirect
from users.models import User
from .models import Client


def clients_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        user = request.user
        print(user)

        if user.is_client():
            client = Client.objects.get(user=user)

            request.client = client

            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")

    return wrap
