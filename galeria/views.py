from django.shortcuts import render



def index(request):
    
    dados = {
    1: {"nome": "Nebulosa de Carina", "legenda": "webbtelecope.org / nasa / james webb"},
    2: {"nome": "Galaxia NGC 1079", "legenda": "nasa.org / NASA / hubble"}
    }
    
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')