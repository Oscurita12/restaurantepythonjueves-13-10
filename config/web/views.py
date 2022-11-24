from django.shortcuts import render
from django.shortcuts import redirect
from web.formularios.formularioPersonal import FormularioPersonal
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos

#Importar el formulario a render
from web.formularios.formularioPlatos import FormularioPlatos
# Create your views here.
#Las vistas en Django son los CONTROLADORES 

from web.models import Platos, Empleado


#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):

    platosConsultados=Platos.objects.all()

    formulario=FormularioEdicionPlatos()

    diccionarioEnvio={
        'platos': platosConsultados,
        'formulario': formulario 
    }

    return render (request, 'menuPlatos.html', diccionarioEnvio)

def EditarPlato(request,id):
    print(id)
    #Recibir los datos del formulario y editar mi plato 
    if request.method=='POST':
        datosDelFormulario=FormularioEdicionPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato=datosDelFormulario.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(precio=datosPlato["precioPlato"])
                print("EXITO EDITANDO EL PLATO")

            except Exception as error:
                
                print("error",error)

    return redirect('menu')

def MenuEmpleados(request):
    empleadosConsultados=Empleado.objects.all()

    diccionarioEmpleado={
        'empleados': empleadosConsultados
    }
    print(diccionarioEmpleado)

    return render (request, 'menuEmpleados.html', diccionarioEmpleado)

def VistaPlatos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
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
            #creamos un objeto del ripo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
            )
            #intentamos llevar el objeto platoNuevo a la BD
            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error",error)

    return render(request, 'platos.html', datosParaTemplate)


def VistaPersonal(request):  

    formulario=FormularioPersonal()
    datosParaPersonal={
        'formularioPersonal':formulario,
        'bandera':False
    }

    if request.method=='POST':
        print("Hola")
        datosDelPersonal=FormularioPersonal(request.POST)
        #print(datosDelPersonal)
        if datosDelPersonal.is_valid():
            print("oe")
            datosPersonal=datosDelPersonal.cleaned_data
            print(datosPersonal)
            #creamos un objeto del tipo MODELO PERSONAL
            personalNuevo=Empleado(
                nombre_empleado=datosPersonal["nombreEmpleado"],
                apellidos_empleado=datosPersonal["apellidoEmpleado"],
                foto_empleado=datosPersonal["fotoEmpleado"],
                cargo_empleado=datosPersonal["cargoEmpleado"],
                salario_empleado=datosPersonal["salarioEmpleado"],
                contacto_empleado=datosPersonal["contactoEmpleado"]
            )
            #intentamos llevar el objeto platoNuevo a la BD
            try:
                personalNuevo.save()
                datosParaPersonal["bandera"]=True
                print("EXITO GUARDANDO EL EMPLEADO")

            except Exception as error:
                datosParaPersonal["bandera"]=False
                print("error",error)
            
    return render(request, 'personal.html',datosParaPersonal)