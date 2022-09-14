from django.http import HTTPResponse
from django.db import modelos

def madre(request):
    return HTTPResponse("nombre de Mama" )

def hermano(request):
    return HTTPResponse("Nombre Hermano")