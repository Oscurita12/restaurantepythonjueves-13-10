#Los formularios de django son clases 

from secrets import choice
from tkinter.tix import Select
from django import forms


class FormularioPersonal(forms.Form): 

    #Creando atributo para cargar el selector

    OPCIONES=(
        (1, 'Medellin'),
        (2, 'Envigado'),
        (3, 'Itagui'),
        (4, 'Sabaneta'),
        (5, 'Bello')
    )
    
    #Dentro de la clase cada atributo será un input 

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=5
    )

    identificacionEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control m-b3'}),
        required=True,
        max_length=20
    )

    direccionEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
    )

    municipioEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES
    )

    correoEmpleado=forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control mb-3'}),
        required=True
    )

    telefonoEmpleado=forms.CharField(
        widget=forms.NumberInput (attrs={'class':'form-control mb-3'}),
        required=True,
    )

    