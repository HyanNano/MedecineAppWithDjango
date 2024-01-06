from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required

from django.conf import settings
import googlemaps

from .models import Medicament,Actualite,Pharmacie
from .forms import MedocForm,ActuForm

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
  
 
 
def calcul_distance(origine, destination):
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    
    result = gmaps.distance_matrix(origine, destination, units='metric')
    distance = result['rows'][0]['elements'][0]['distance']['text']
    duree = result['rows'][0]['elements'][0]['duration']['text']
   
    distance_duree = { "distance" : distance , "duree" : duree }
    
    return distance_duree


def test_distance(request):
    dist = calcul_distance( "etoug-ebe, Yaounde", (3.8405788, 11.4782645))
    
    return render(request, "MedecineApp/distance.html", {"dist" : dist })
 
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
                    if medicament.quantite > 0 :
                        #Trouver la pharmacie du medoc
                        pharmacie = Pharmacie.objects.get( nom_pharmacie = medicament.nom_pharmacie)
                        
                        #Calcul de la distance a l'emplacement
                        destination_longitude = pharmacie.longitude
                        destination_latitude = pharmacie.latitude
                        distance_duree = calcul_distance( emplacement, (destination_latitude, destination_longitude))
                        
                        medicament_distance = {"medicament" : medicament, 
                                            "distance" : distance_duree['distance'] , 
                                            "duree" : distance_duree['duree'] }
                        
                        list_medicaments.append(medicament_distance)

    
            #return it such as we can use the result in our search page
            return render(request, 'MedecineApp/search.html', {"list_medicaments": list_medicaments, "medoc_form":medoc_form, 'api_key': settings.GOOGLE_API_KEY})
        

    # if a GET (or any other method) we'll create a blank form
    else:
        medoc_form = MedocForm()
        
        

    return render(request, "MedecineApp/search.html", {"medoc_form": medoc_form})

@permission_required("MedecineApp.add_actualite",raise_exception=True)
def publish(request):
    
    if request.method == "POST":
        actu_form = ActuForm(request.POST)
        if actu_form.is_valid():
            #process
            actu_title = actu_form.cleaned_data["title"]
            actu_author = actu_form.cleaned_data["author"]
            actu_date = actu_form.cleaned_data["date"]
            actu_content = actu_form.cleaned_data["content"]
            
            actu = Actualite.objects.create(titre=actu_title, auteur=actu_author, date_publication=actu_date, contenu=actu_content)
            
            actu_form = ActuForm()            
    else:
        actu_form = ActuForm()
        
    return render(request, "MedecineApp/publish.html", {"actu_form": actu_form})


def login_user(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password =request.POST["password"]

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)

            return redirect("index") 
        else :
            messages.info(request,"identifiant ou mot de passe incorrecte")     
    form= AuthenticationForm()
    return render(request,"MedecineApp/login.html",{"form":form })


def logout_user(request):
    logout(request)

    return redirect("index") 

def register_user(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index") 
    else:
        form= UserCreationForm()

    return render(request,"MedecineApp/register.html",{"form":form })            


def actualite(request):
    pass

def affichage_routes(request):
    context = {
        'api_key': settings.GOOGLE_API_KEY
    }
    return render(request, 'MedecineApp/route.html', context)
