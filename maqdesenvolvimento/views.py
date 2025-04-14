from django.shortcuts import render, get_object_or_404
from maqdesenvolvimento.models import MaqDesenvolvimento

def emdesenvolvimento(request):
    emdesenvolvimento = MaqDesenvolvimento.objects.all() 
    return render(request, 'maqdesenvolvimento/index.html', {"cards": emdesenvolvimento})

def imgdes(request, imgdes_id):
    imgdes = get_object_or_404(MaqDesenvolvimento, pk=imgdes_id)
    return render(request, 'maqdesenvolvimento/imagem.html', {"imgdes": imgdes})
