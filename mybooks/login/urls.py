from django.urls import path

from . import views

urlpatterns = [
    path("login", views.loginView),
    path("logout", views.logoutView),
]
