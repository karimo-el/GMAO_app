from django import forms
from .models import work_request
from datetime import date
class handel_create_dt_form(forms.ModelForm):
    class Meta:
        model = work_request
        fields = ['number_DT', 'first_name',  "last_name", "equipement", "installation", 'anomlie', "service_conserne",'date_creation' ]
        labels = {
                'number_DT'       : 'N°_DT', 
                'first_name'      : 'Nom', 
                "last_name"       : 'Prenom', 
                "equipement"      : 'Equipement', 
                "installation"    : "Installation", 
                'anomlie'         : "Anomalie", 
                "service_conserne": "Nature d'intervention", 

                'date_creation'   : 'Date de creation'
        }
        sevice = [
    ('Electrique', 'Electrique'),
    ('Mécanique', 'Mécanique'),
    ('Commun', 'Commun'),
    
]
        widgets = {
            'number_DT' : forms.NumberInput(attrs={ "class": 'form-control' , 'readonly':True}),
            'first_name' : forms.TextInput(attrs= {'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'equipement': forms.TextInput(attrs = {'class': 'form-control'}),
            'installation': forms.TextInput(attrs = {'class': 'form-control'}),
            'anomlie' : forms.Textarea( attrs={  'class': 'form-control', 'style': 'margin-bottom: 10px'}),
            'date_creation': forms.DateInput(format=('%y/%m/%d'), attrs={'class': 'form-control',  'type': 'date' , 'value': date.today().strftime("%Y-%m-%d")}),
            

        }
class handel_update_dt_form(forms.ModelForm):
    class Meta:
        model = work_request
        fields = ['number_DT', 'first_name',  "last_name", "equipement", "installation", 'anomlie', "service_conserne",'date_creation' ]
        labels = {
                'number_DT'       : 'N°_DT', 
                'first_name'      : 'Nom', 
                "last_name"       : 'Prenom', 
                "equipement"      : 'Equipement', 
                "installation"    : "Installation", 
                'anomlie'         : "Anomalie", 
                "service_conserne": "Nature d'intervention", 

                'date_creation'   : 'Date de creation'
        }
        sevice = [
    ('Electrique', 'Electrique'),
    ('Mécanique', 'Mécanique'),
    ('Commun', 'Commun'),
    
]
        widgets = {
            'number_DT' : forms.NumberInput(attrs={ "class": 'form-control' , 'readonly':True}),
            'first_name' : forms.TextInput(attrs= {'class': 'form-control', "readonly":True}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control', "readonly":True}), 
            'equipement': forms.TextInput(attrs = {'class': 'form-control'}),
            'installation': forms.TextInput(attrs = {'class': 'form-control'}),
            'anomlie' : forms.Textarea( attrs={  'class': 'form-control', 'style': 'margin-bottom: 10px'}),
             'date_creation': forms.DateInput( attrs={'class': 'form-control', "readonly":True}),
            

        }
