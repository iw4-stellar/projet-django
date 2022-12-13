from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .forms import BooksellerRegistrationForm, ClientRegistrationForm
# Create your views here.

def loginView(request):
  context = {}
  return HttpResponse(render(request, 'login/login.html', context))

def registerBooksellerView(request):
  if request.method == 'POST':
    form = BooksellerRegistrationForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']

      # Create user with email & password
      user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
      )

      # Add user to clients group
      bookseller_group, _ = Group.objects.get_or_create(name='bookseller')
      user.groups.add(bookseller_group)

      # Save changes
      user.save()

    return HttpResponseRedirect('/')

  form = BooksellerRegistrationForm()

  context = {
    'form': form,
  }
  return HttpResponse(render(request, 'login/register-bookseller.html', context))

def registerClientView(request):
  if request.method == 'POST':
    form = ClientRegistrationForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']

      # Create user with email & password
      user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
      )

      # Add user to clients group
      client_group, _ = Group.objects.get_or_create(name='client')
      user.groups.add(client_group)

      # Save changes
      user.save()

    return HttpResponseRedirect('/')

  form = ClientRegistrationForm()

  context = {
    'form': form,
  }
  return HttpResponse(render(request, 'login/register-client.html', context))
