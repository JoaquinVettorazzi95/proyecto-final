from django.shortcuts import render
from ejemplo.models import Familiar


def index(request):
    return render (request, "ejemplo/saludar.html")

def saludar_a(request,nombre):
    return render (request,
    "ejemplo/saludar_a.html",
    {"nombre": nombre}
    )

def sumar(request, a, b):
    return render (request,
    "ejemplo/sumar.html",
    {"a": a,
     "b": b,
     "resultado": a + b
    }
    )

def buscar(request):
    query = request.GET["q"]
    return render(request, "ejemplo/buscar.html", {"query": query})

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares" : lista_familiares})