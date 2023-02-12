from django.urls import path
from . import views

app_name = "reading_groups"

urlpatterns = [
    path("", views.indexView),
    path("create/", views.createView),
    path("<int:id>/", views.detailView, name="detail"),
]
