from django.urls import path
from apps.maqdesenvolvimento.views import emdesenvolvimento, imgdes

urlpatterns = [
    path('emdesenvolvimento', emdesenvolvimento, name='emdesenvolvimento'),
    path('imgdes/<int:imgdes_id>', imgdes, name='imgdes'),
    #path('buscar', buscar, name="buscar"),
]