from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello_World")

def mostrar_nombre(request):
    return HttpResponse("Deymian Gustavo Zapata Rodríguez") 
def home_page(request):  # <-- Agrega esta función
    return HttpResponse("¡Bienvenido a mi tarea :) !")