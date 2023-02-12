from django.urls import path

from . import views

app_name = "bookseller"

urlpatterns = [
    path("", views.indexView),
    path("inventory/", views.inventoryView),
    path("inventory/add/", views.addInvetoryItemView),
    path(
        "inventory/<int:id>/delete", views.deleteInventoryView, name="inventory-delete"
    ),
]
