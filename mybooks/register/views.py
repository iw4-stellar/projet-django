from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.models import User
from client.models import Client
from bookseller.models import Bookseller
from .forms import BooksellerRegistrationForm, ClientRegistrationForm


# Create your views here.


def registerBooksellerView(request):
    template = "login/register-bookseller.html"

    if request.method == "POST":
        form = BooksellerRegistrationForm(request.POST)
        context = {
            "form": form,
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            name = form.cleaned_data.get("name", "").strip()

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=User.Type.BOOKSELLER,
            )

            bookseller = Bookseller.objects.create(
                user=user,
                name=name,
            )

            login(request, user)

            return redirect("/bookseller")
        else:
            return render(request, template, context)
    else:
        form = BooksellerRegistrationForm()
        context = {
            "form": form,
        }
        return render(request, template, context)


def registerClientView(request):
    template = "login/register-client.html"

    if request.method == "POST":
        form = ClientRegistrationForm(request.POST)
        context = {
            "form": form,
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            name = form.cleaned_data.get("name", "").strip()

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=User.Type.CLIENT,
            )

            client = Client.objects.create(
                user=user,
                name=name,
            )

            login(request, user)

            return redirect("/client")
        else:
            return render(request, template, context)
    else:
        form = ClientRegistrationForm()
        context = {
            "form": form,
        }
        return render(request, template, context)
