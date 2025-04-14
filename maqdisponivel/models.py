from django.db import models

from datetime import datetime

class Maquina(models.Model):
    
    OPCOES_CATEGORIA = [
        ("TRATOR", "Trator" ),
        ("IMPLEMENTO AGRÍCOLA", "Implemento Agrícola" ),
    ]
    
    nome = models.CharField(max_length=100, null=True, blank=True) 
    descricao = models.TextField(null=True, blank=True) 
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='') 
    operacao_agricola = models.CharField(null=True, blank=True)     
    tipo = models.CharField(max_length=100, null=True, blank=True) 
    cadeia_produtiva = models.CharField(max_length=100, null=True, blank=True)
    codigo_produto = models.CharField(max_length=100, null=True, blank=True) 
    codigo_finame = models.CharField(max_length=100, null=True, blank=True, default='') 
    hp = models.CharField(null=True, blank=True)     
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    link_pagina = models.CharField(max_length=100, null=True, blank=True)
    empresa = models.CharField(max_length=100, null=True, blank=True)
    publicada = models.BooleanField(default=False)
    data_registro = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nome
    
    
