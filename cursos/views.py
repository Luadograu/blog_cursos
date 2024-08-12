from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    return render(request, 'cursos/cursos.html')

def alimentos(request):
    return render(request, 'cursos/alimentos.html')

def quimica(request):
    return render(request, 'cursos/quimica.html')

def ads(request):
    return render(request, 'cursos/ads.html')