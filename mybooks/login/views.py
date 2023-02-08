from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import User
from .forms import LoginForm


# Create your views here.
def logoutView(request):
    logout(request)
    return redirect("/login")


def loginView(request):
    template = "login/login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            identifier = form.cleaned_data["identifier"]
            password = form.cleaned_data["password"]

            try:
                db_user = (
                    User.objects.get(email=identifier)
                    if "@" in identifier
                    else User.objects.get(username=identifier)
                )
                if db_user is not None:
                    user = authenticate(
                        request,
                        username=db_user.username,
                        password=password,
                    )
                    if user is not None:
                        login(request, user)
                        return redirect("/")
                    else:
                        raise User.DoesNotExist()
                else:
                    raise User.DoesNotExist()

            except User.DoesNotExist:
                context["error"] = "Invalid credentials"
                return render(request, template, context)
        else:
            context["error"] = "Invalid input. Try again!"
            return render(request, template, context)
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, template, context)
