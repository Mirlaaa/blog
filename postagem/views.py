from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def noticia(request):
    return render(request, 'noticia.html')

def informatica(request):
    return render(request, 'informatica.html', {
        'nome_curso': 'Informática'
    })

def alimentos(request):
    return render(request, 'alimentos.html', {
        'nome_curso': 'Alimentos'
    })

def apicultura(request):
    return render(request, 'apicultura.html', {
        'nome_curso': 'Apicultura'
    })

def quimica(request):
    return render(request, 'quimica.html', {
        'nome_curso': 'Química'
    })

def ads(request):
    return render(request, 'ads.html', {
        'nome_curso': 'Análise e Desenvolvimento de Sistemas'
    })

def agroindustria(request):
    return render(request, 'agroindustria.html', {
        'nome_curso': 'Agroindústria'
    })

