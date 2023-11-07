from django.contrib import admin
from .models import Utilisateur, Medicament, Pharmacie, Actualite

# Register your models here.

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
  list_display=("nom","prenom","mot_de_passe")
  
@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
  list_display=("nom_medicament","quantite","date_expiration","nom_pharmacie")


@admin.register(Pharmacie)
class PharmacieAdmin(admin.ModelAdmin):
   list_display=("nom_pharmacie","heure_ouverture","heure_fermeture","longitude","latitude")

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
  list_display=("titre","auteur","date_publication","contenu")
  