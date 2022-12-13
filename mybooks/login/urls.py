from django.urls import path

from . import views

urlpatterns = [
  path('login', views.loginView),
  path('register/bookseller', views.registerBooksellerView),
  path('register/client', views.registerClientView),
]