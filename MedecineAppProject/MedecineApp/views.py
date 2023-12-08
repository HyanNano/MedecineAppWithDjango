from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Medicament
from .forms import MedocForm

# Create your views here.

""" def get_medicament_by_id(id):
    return Medicament.objects.get(id_medicament=id)

def filter_medicaments_by_nom(nom):
    return Medicament.objects.filter(nom_medicament=nom)

def filter_medicaments_by_quantite(nombre):
    return Medicament.objects.filter(quantite__gt=nombre)

def order_medicaments_by_date_expiration():
    return Medicament.objects.order_by('date_expiration')
"""
""" 
def add(request):
    parmacie=Pharmacie.objects.get(nom_pharmacie="pharmacie du soleil")
    med=Medicament.objects.create(nom_medicament="Gentamicine",quantite=40,date_expiration="2020-12-28",nom_pharmacie=parmacie)
    return redirect("MedecineApp:index")

def update(request):
    med=Medicament.objects.get(nom_medicament="paracetamol") 
    med.nom_medicament="arthemetere"
    med.save()
    return redirect("MedecineApp:index")
    
def delete(request):
    med=Medicament.objects.get(nom_medicament="arthemetere") 
    med.delete() 
    return redirect("MedecineApp:index")
"""
 
def index(request):
    context={"Medicament": Medicament.objects.all()}
    return render(request,'MedecineApp/index.html', context)
   
def rechercher(request):
    context={"Medicament": Medicament.objects.all()}
    return render(request,'MedecineApp/rechercher.html', context)
  
  
def search(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        medoc_form = MedocForm(request.POST)
        # check whether it's valid:
        if medoc_form.is_valid():
            # process the data in form.cleaned_data as required
            medoc_name = medoc_form.cleaned_data["medoc_name"]
            emplacement = medoc_form.cleaned_data["emplacement"]
            
            #put those medicaments in a list
            list_medicaments = []
    
            #search through our table Medicament all the medicaments which have medoc_name in their names
                ##medoc = Medicament.objects.get(medoc_name is in nom_medicament)
    
            medicaments = Medicament.objects.all()
            for medicament in medicaments:
                if medoc_name in medicament.nom_medicament:
                    list_medicaments.append(medicament)
    
            #return it such as we can use the result in our search page
            return render(request, 'MedecineApp/search.html', {"list_medicaments": list_medicaments, "medoc_form":medoc_form})

            # redirect to a new URL:
            #return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        medoc_form = MedocForm()
        

    return render(request, "MedecineApp/search.html", {"medoc_form": medoc_form})