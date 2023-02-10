from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.models import Client, Bookseller
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
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            try:
                if password != confirm_password:
                    raise Exception("Passwords don't match")

                username_exists = Bookseller.objects.filter(username=username).exists()
                if username_exists:
                    raise Exception("Username already in use")

                email_exists = Bookseller.objects.filter(email=email).exists()
                if email_exists:
                    raise Exception("Email address already in use")

                user = Bookseller.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )

                login(request, user)

                return redirect("/")
            except Exception as e:
                error = e.args[0]
                context["error"] = error
            finally:
                return render(request, template, context)

        else:
            context["error"] = "Invalid input. Try again!"
            return render(request, template, context)

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
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            try:
                if password != confirm_password:
                    raise Exception("Passwords don't match")

                username_exists = Client.objects.filter(username=username).exists()
                if username_exists:
                    raise Exception("Username already in use")

                email_exists = Client.objects.filter(email=email).exists()
                if email_exists:
                    raise Exception("Email address already in use")

                user = Client.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )

                login(request, user)

                return redirect("/")
            except Exception as e:
                error = e.args[0]
                context["error"] = error
            finally:
                return render(request, template, context)

        else:
            context["error"] = "Invalid input. Try again!"
            return render(request, template, context)

    form = ClientRegistrationForm()
    context = {
        "form": form,
    }
    return render(request, template, context)
