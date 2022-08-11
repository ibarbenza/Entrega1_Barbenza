from django.shortcuts import render
from RDC_App.models import *
from RDC_App.forms import Search

# Create your views here.

def index(request):

    vinos = Vinos.objects.all().order_by("bodega")

    if request.GET.get("nombre_producto"):
        
        formulario = Search(request.GET)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            vinos = vinos.filter(bodega__icontains = data["nombre_producto"]).order_by("etiqueta")
            context = {"vinos" : vinos, "number" : 30, "formulario" : formulario} 
        
            return render(request, "RDC_App/index.html", context)

    else:
        formulario = Search()
        context = {"vinos" : vinos, "number" : 30, "formulario" : formulario, "response": "El producto buscado no existe. Intente devuelta!"} 
        return render(request, "RDC_App/index.html", context)

def reseña(request):
    return render(request, 'RDC_App/reseña.html')


    