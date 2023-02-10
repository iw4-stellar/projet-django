from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReadingGroupCreationForm
from .models import ReadingGroup

# Create your views here.
def indexView(request):
  template = 'reading_groups/index.html'
  
  reading_groups = ReadingGroup.objects.all()
  context = {
    "reading_groups": reading_groups,
  }

  return render(request, template, context)

def detailView(request, id):
  template = 'reading_groups/detail.html'
  rg = ReadingGroup.objects.filter(id=id).first()
  context = {
    "rg": rg
  }

  return render(request, template, context)

@login_required
def createView(request):
  template = 'reading_groups/create.html'

  if request.method == 'POST':
    form = ReadingGroupCreationForm(request.POST)
    context = {
      "form": form,
    }

    if form.is_valid():
      title = form.cleaned_data["title"]
      capacity = form.cleaned_data["capacity"]

      bookseller = request.user

      rg = ReadingGroup.objects.create(
        title=title,
        capacity=capacity,
        bookseller=bookseller,
      )
      
      return redirect("/reading-groups")
    else:
      context["error"] = "Invalid input"

      return render(request, template, context)

  form = ReadingGroupCreationForm()
  context = {
    "form": form,
  }

  return render(request, template, context)