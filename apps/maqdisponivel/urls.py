from django.urls import path
from apps.maqdisponivel.views import index, imagem, buscar, filtro_etapa, filtro_natureza

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:maquina_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path("filtro_etapa/<str:etapa>", filtro_etapa, name="filtro_etapa"),
    path("filtro_natureza/<str:natureza>", filtro_natureza, name="filtro_natureza"),
]
