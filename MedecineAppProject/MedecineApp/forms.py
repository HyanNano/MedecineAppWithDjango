from django import forms

class MedocForm(forms.Form):
    medoc_name = forms.CharField(label="Medecine name", max_length=100)
    emplacement = forms.CharField(label="Emplacement", max_length=100)
    
class ActuForm(forms.Form):
    title = forms.CharField(label="Actualite Title", max_length=300)
    author = forms.CharField(label="Actualite Auteur", max_length=300)
    date = forms.DateField(label="Actualite Date")
    content = forms.CharField(label="Actualite Contenu")
    