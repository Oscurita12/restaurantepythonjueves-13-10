from django.shortcuts import render
from web.formularios.formularioPersonal import FormularioPersonal

#Importar el formulario a render
from web.formularios.formularioPlatos import FormularioPlatos
# Create your views here.
#Las vistas en Django son los CONTROLADORES 

#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')


def Platos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario
    }

    #Preguntamos si existe alguna petición de tipo POST asciada a la vista
    if request.method=='POST':
        #Deberíamos capturar los datos del formulario 
        datosDelFormulario=FormularioPlatos(request.POST)
        #Verificarsi los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #Capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            print(datosDelFormulario)
            print(datosPlato)

    return render(request, 'platos.html', datosParaTemplate)


def Personal(request):  

    formulario=FormularioPersonal()
    datosParaPersonal={
        'formularioPersonal':formulario
    }

    if request.method=='POST':
        print("Hola")
        datosDelPersonal=FormularioPersonal(request.POST)
        #print(datosDelPersonal)
        if datosDelPersonal.is_valid():
            print("oe")
            datosPersonal=datosDelPersonal.cleaned_data
            print(datosPersonal)
            
    return render(request, 'personal.html',datosParaPersonal)