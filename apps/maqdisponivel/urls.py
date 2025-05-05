from django.urls import path
from apps.maqdisponivel.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:maquina_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
]
