from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Medicament

# Create your views here.

def index(request):
    context={"Medicament": Medicament.objects.all()}
    return render(request,'MedecineApp/Frontend/accueil.html', context)

def get_medicament_by_id(id):
    return Medicament.objects.get(id_medicament=id)

def filter_medicaments_by_nom(nom):
    return Medicament.objects.filter(nom_medicament=nom)

def filter_medicaments_by_quantite(nombre):
    return Medicament.objects.filter(quantite__gt=nombre)

def order_medicaments_by_date_expiration():
    return Medicament.objects.order_by('date_expiration')