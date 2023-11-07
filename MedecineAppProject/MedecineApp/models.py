from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

class Pharmacie(models.Model):
    id_pharmacie = models.AutoField(primary_key=True)
    nom_pharmacie = models.CharField(max_length=100)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    def __str__(self):
        return self.nom_pharmacie   

class Medicament(models.Model):
    id_medicament = models.AutoField(primary_key=True)
    nom_medicament = models.CharField(max_length=100)
    quantite = models.IntegerField(default=0)
    date_expiration = models.DateField()
    nom_pharmacie = models.ForeignKey(Pharmacie,on_delete=models.DO_NOTHING)


class Actualite(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    date_publication = models.DateField()
    contenu = models.TextField()