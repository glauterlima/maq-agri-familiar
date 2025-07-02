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
        ("PÓS-COLHEITA", "Pós-Colheita" ),
       
    ]
    
    OPCOES_NATUREZA = [
        ("TRATORES", "Tratores" ),
        ("PULVERIZADOR_AGRICOLA", "Pulverizador Agrícola" ),
        ("MÁQUINAS E APARELHOS PARA PREPARAÇÃO, TRABALHO DO SOLO OU CULTURA", "Máquinas e aparelhos para preparação, trabalho do solo ou cultura" ),
          
    ]
    
    OPCOES_FREQUENCIA_USO = [
        ("ESPORÁDICA", "Esporádica" ),
        ("DIÁRIA", "Diária" ),
        ("SEMANAL", "Semanal" ),
        ("MENSAL", "Mensal" ),
        ("TRIMESTRAL", "Trimestral" ),
        ("SEMESTRAL", "Semestral" ),
        ("ANUAL", "Anual" ),  
          
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
    natureza = models.TextField(null=True, choices=OPCOES_NATUREZA, blank=True)
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
    
    """variáveis criadas para atender a tabela de máquinas sociobiodiversidade"""
    utilizacao = models.CharField(max_length=500, null=True, blank=True)
    produto_linha_producao = models.CharField(max_length=200, null=True, blank=True)
    insumos_item = models.CharField(max_length=500, null=True, blank=True)
    local_aquisicao_item = models.CharField(max_length=500, null=True, blank=True)
    ano_aquisicao_item = models.DateTimeField(null=True, default=datetime.now, blank=True)
    caracteristicas_detalhadas_item = models.TextField(null=True, blank=True)
    aspectos_item_boas_praticas = models.TextField(null=True, blank=True)
    item_gera_residuo = models.BooleanField(null=True, default=False)
    qual_residuo = models.CharField(max_length=200, null=True, blank=True)
    #preco_min_item = models.DecimalField(max_length=100, null=True, blank=True)
    #preco_max_item = models.DecimalField(max_length=100, null=True, blank=True)
    impacto_positivo_item = models.TextField(null=True, blank=True)
    condicoes_adequadas_uso = models.TextField(null=True, blank=True)
    tipo_uso_item = models.CharField(max_length=200, null=True, blank=True)
    faz_manutencao_item = models.BooleanField(null=True, default=False)
    frequencia_uso_item = models.CharField(null=True, max_length=100, choices=OPCOES_FREQUENCIA_USO, default='')
    problema_item_12_meses = models.CharField(max_length=200, null=True, blank=True)
    frequencia_manutencao_item_12_meses = models.CharField(max_length=200, null=True, blank=True)
    capacitacao_manutencao_item = models.BooleanField(null=True, default=False)
    tempo_uso_item_mes = models.CharField(max_length=200, null=True, blank=True)
    
    observacoes = models.TextField(null=True, blank=True)
 
    
     
    
    
    
    def __str__(self):
        return self.nome
    
    
