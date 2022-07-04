from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def informatica(request):
    return render(request, "informatica.html")

def noticia(request):
    return render(request, "noticia.html")