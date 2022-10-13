from django.shortcuts import render

# Create your views here.
#Las vistas en Django son los CONTROLADORES 

#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')