#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#funcion que recibe como parametro un http request y devuelve como parametro otro http request 

def hello(request):
    return HttpResponse("hola mundo")

#el nombre de la funcion y la url no es necesario que sean iguales, simplemente llamarlas en donde se utilice como en cualquier funcion 