from django.urls import path
from apps.fornecedores.views import fornecedores


urlpatterns = [
    path('fornecedores', fornecedores, name='fornecedores'), #path(url, método da view, como acessar)
 
]