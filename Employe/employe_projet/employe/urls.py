from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employes, name = "list_employes"),
]