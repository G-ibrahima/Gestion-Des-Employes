from django.shortcuts import render

from .models import *
# Create your views here.

def list_employes(request):
    employes = Employe.objects.all()
    return render(request,'employe/list.html', {'employes' : employes})