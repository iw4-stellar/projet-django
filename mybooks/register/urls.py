from django.urls import path

from . import views

urlpatterns = [
    path("register/bookseller", views.registerBooksellerView),
    path("register/client", views.registerClientView),
]
