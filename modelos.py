from django.db import modelos


def Familia(request):
    madre = family(nombre = "Maria", edad = "58",)
    madre.save(nombre,edad),
    
    hermano = family(nombre1 = "luis", edad1 = "18",)
    hermano.save(nombre1, edad1),
    