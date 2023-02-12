from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.indexView),
    path("<int:id>/", views.bookView, name="book"),
    path("add_book/", views.add_book),
]
