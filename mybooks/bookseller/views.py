from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import booksellers_only
from loan.models import Inventory, InventoryItem
from loan.forms import InventoryItemForm


# Create your views here.
@login_required
@booksellers_only
def indexView(request):
    template = "bookseller/index.html"
    return render(request, template)


@login_required
@booksellers_only
def inventoryView(request):
    template = "bookseller/inventory.html"
    bookseller = request.bookseller

    inventory = Inventory.objects.filter(bookseller=bookseller).first()
    items = InventoryItem.objects.filter(inventory=inventory)

    context = {
        "inventory": inventory,
        "items": items,
    }
    return render(request, template, context)


@login_required
@booksellers_only
def addInvetoryItemView(request):
    template = "bookseller/add.html"

    if request.method == "POST":
        form = InventoryItemForm(request.POST)

        if form.is_valid():
            bookseller = request.bookseller
            inventory = Inventory.objects.filter(bookseller=bookseller).first()

            item = form.save(commit=False)
            item.inventory = inventory

            form.save()

            return redirect("/bookseller/inventory")

    form = InventoryItemForm()
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
@booksellers_only
def deleteInventoryView(request, id):
    item = InventoryItem.objects.filter(id=id).first()
    bookseller = request.bookseller

    if bookseller == item.inventory.bookseller:
        item.delete()

    return redirect("/bookseller/inventory")
