from django import forms

class MedocForm(forms.Form):
    medoc_name = forms.CharField(label="Medoc name", max_length=100)
    emplacement = forms.CharField(label="Emplacement", max_length=100)