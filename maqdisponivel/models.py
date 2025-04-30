from django.db import models

from datetime import datetime

class Maquina(models.Model):
    
    OPCOES_CATEGORIA = [
        ("TRATOR", "Trator" ),
        ("IMPLEMENTO AGRÍCOLA", "Implemento Agrícola" ),
    ]
    
    OPCOES_TEMA = [
        ("GRÃOES E FORRAGENS", "Grãos e Forragens" ),
        ("HORTICULTURA", "Horticultura" ),
        ("FRUTÍFERAS", "Frutíferas" ),
        ("TODAS", "Todas" ),
        ("OUTROS", "Outros" ),
    ]
    
    OPCOES_FUNCAO = [
        ("PRODUTIVA", "Produtiva" ),
       
    ]
    
    OPCOES_ETAPA = [
        ("PLANTIO", "Plantio" ),
        ("PREPARO DE SOLO", "Preparo de Solo" ),
        ("COLHEITA", "Colheita" ),
        ("PLANTIO", "Plantio" ),
        ("PÓS-COLHEITA", "Pós-Colheita" ),
       
    ]
    
    codigo_finame = models.CharField(max_length=100, null=True, blank=True, default='') 
    nome = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)  
    descricao = models.TextField(null=True, blank=True) 
    linha_financiamento = models.TextField(null=True, blank=True)
    cnpj_fabricante = models.CharField(max_length=50, null=True, blank=True)
    nome_fabricante = models.CharField(max_length=100, null=True, blank=True)
    ncm = models.CharField(max_length=50, null=True, blank=True)
    ncm_descricao = models.TextField(null=True, blank=True)
    natureza = models.TextField(null=True, blank=True)
    link_pagina = models.CharField(max_length=100, null=True, blank=True)
    tema = models.CharField(null=True, max_length=100, choices=OPCOES_TEMA, default='')
    cultura = models.TextField(null=True, blank=True)
    funcao = models.CharField(null=True, max_length=100, choices=OPCOES_FUNCAO, default='')
    etapa = models.CharField(null=True, max_length=100, choices=OPCOES_ETAPA, default='')
    
    categoria = models.CharField(null=True, max_length=100, choices=OPCOES_CATEGORIA, default='') 
    operacao_agricola = models.CharField(null=True, blank=True)     
    tipo = models.CharField(max_length=100, null=True, blank=True) 
    cadeia_produtiva = models.CharField(max_length=100, null=True, blank=True)
    codigo_produto = models.CharField(max_length=100, null=True, blank=True)     
    hp = models.CharField(null=True, blank=True)     
    foto = models.ImageField(null=True, upload_to="fotos/%Y/%m/%d/", blank=True)    
    empresa = models.CharField(max_length=100, null=True, blank=True)
    publicada = models.BooleanField(null=True, default=False)
    data_registro = models.DateTimeField(null=True, default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nome
    
    
