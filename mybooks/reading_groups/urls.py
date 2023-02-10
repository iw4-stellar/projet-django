from django.urls import path
from . import views

app_name = 'reading_groups'

urlpatterns = [
  path('', views.indexView),
  path('<int:id>/', views.detailView, name='detail'),
  path('create/', views.createView),
]