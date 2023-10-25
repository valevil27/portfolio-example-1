from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Mi web personal </h1><h2>Portada</h2>")

def about(request):
    return HttpResponse("<h1> Mi web personal </h1><h2>Acerca de</h2>")