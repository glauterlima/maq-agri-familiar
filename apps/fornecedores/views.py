from django.shortcuts import render
from django.http import HttpResponse

def fornecedores(request):
    return render(request, 'fornecedor/index.html')