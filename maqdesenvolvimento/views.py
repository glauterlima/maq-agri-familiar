from django.shortcuts import render, get_object_or_404, redirect
from maqdesenvolvimento.models import MaqDesenvolvimento
from django.contrib import messages

def emdesenvolvimento(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
        
    emdesenvolvimento = MaqDesenvolvimento.objects.order_by("nome").filter(publicada=True)  
    return render(request, 'maqdesenvolvimento/index.html', {"cards": emdesenvolvimento})

def imgdes(request, imgdes_id):
    imgdes = get_object_or_404(MaqDesenvolvimento, pk=imgdes_id)
    return render(request, 'maqdesenvolvimento/imagem.html', {"imgdes": imgdes})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    
    maquinas = MaqDesenvolvimento.objects.order_by("nome").filter(publicada=True)  
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            maquinas = maquinas.filter(nome__icontains=nome_a_buscar)
    
    return render(request, "maqdesenvolvimento/buscar.html", {"cards": maquinas})
