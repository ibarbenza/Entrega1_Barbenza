from django.shortcuts import render
from RDC_App.models import *
from RDC_App.forms import Search, Form_Reseña
from django.shortcuts import redirect

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

def bebidas(request):

    vinos = Bebidas.objects.all().order_by("marca")

    if request.GET.get("nombre_producto"):
        
        formulario = Search(request.GET)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            vinos = vinos.filter(clase__icontains = data["nombre_producto"]).order_by("etiqueta")
            context = {"vinos" : vinos, "number" : 30, "formulario" : formulario} 
        
            return render(request, "RDC_App/bebidas.html", context)

    else:
        formulario = Search()
        context = {"vinos" : vinos, "number" : 30, "formulario" : formulario, "response": "El producto buscado no existe. Intente devuelta!"} 
        return render(request, "RDC_App/bebidas.html", context)

def copas(request):

    vinos = Copas.objects.all().order_by("nombre")

    if request.GET.get("nombre_producto"):
        
        formulario = Search(request.GET)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            vinos = vinos.filter(clase__icontains = data["nombre_producto"]).order_by("etiqueta")
            context = {"vinos" : vinos, "number" : 30, "formulario" : formulario} 
        
            return render(request, "RDC_App/copas.html", context)

    else:
        formulario = Search()
        context = {"vinos" : vinos, "number" : 30, "formulario" : formulario, "response": "El producto buscado no existe. Intente devuelta!"} 
        return render(request, "RDC_App/copas.html", context)


def reseña(request):
    reseñas = Reseña.objects.all().order_by("-fecha")
    return render(request, 'RDC_App/reseña.html', {"reseñas": reseñas})

def add_reseña(request):

    if request.method == "POST":

        miFormulario = Form_Reseña(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            reseña = Reseña(titulo=informacion["titulo"], contenido=informacion["contenido"], rating=informacion["rating"])
            reseña.save()
            return redirect('reseña')

    else:
        miFormulario = Form_Reseña()
    
    return render(request, "RDC_App/add_reseña.html", {"formulario":miFormulario})


    