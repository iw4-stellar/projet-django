from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def loginView(request):
  template = loader.get_template('login/login.html')
  context = {}
  return HttpResponse(template.render(context, request))

def registerBooksellerView(request):
  template = loader.get_template('login/register-bookseller.html')
  context = {}
  return HttpResponse(template.render(context, request))

def registerClientView(request):
  template = loader.get_template('login/register-client.html')
  context = {}
  return HttpResponse(template.render(context, request))
