from django.shortcuts import render, get_object_or_404
from apps.maqdisponivel.models import Maquina


def index(request):  
    maquinas = Maquina.objects.all().filter(publicada=True)   
    #maquinas = Maquina.objects.all().filter(publicada=True)
    #maquinas = Maquina.objects.order_by("-data_registro").filter(publicada=True)    
    return render(request, 'maqdisponivel/index.html', {"cards": maquinas})

def imagem(request, maquina_id):
    maquina = get_object_or_404(Maquina, pk=maquina_id) #Ou encontra o objeto ou aparece um 404
    return render(request, 'maqdisponivel/imagem.html', {"maquina": maquina})

def buscar(request):
    maquinas = Maquina.objects.all().filter(publicada=True) 
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            maquinas = maquinas.filter(nome__icontains=nome_a_buscar)
    
    return render(request, "maqdisponivel/index.html", {"cards": maquinas})

def filtro_etapa(request, etapa):
    maquinas = Maquina.objects.all().filter(publicada=True, etapa__icontains=etapa)
    
    return render(request, 'maqdisponivel/index.html', {"cards": maquinas}) 

def filtro_natureza(request, natureza):
    maquinas = Maquina.objects.all().filter(publicada=True, natureza__icontains=natureza)
    
    return render(request, 'maqdisponivel/index.html', {"cards": maquinas})       

