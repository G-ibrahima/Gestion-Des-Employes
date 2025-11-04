from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_employes, name = "list_employes"),
    path("ajouter/", views.ajouter_employes, name = "ajouter_employes"),
    path("modifier/<int:id>/", views.modifier_employes, name = "modifier_employes"),
    path("supprimer/<int:id>/", views.supprimer_employes, name = "supprimer_employes"),

]