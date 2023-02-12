from django.db import models
from bookseller.models import Bookseller
from books.models import Book
from client.models import Client

# Create your models here.


class Inventory(models.Model):
    bookseller = models.ForeignKey(Bookseller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bookseller.name} inventory"


class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)


class Loan(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


def get_inventory_items(inventory):
    return InventoryItem.objects.filter(inventory=inventory)
