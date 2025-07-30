from django.db import models

from datetime import datetime

from apps.fornecedores.models import Fornecedor

class Maquina(models.Model):
    
    OPCOES_CATEGORIA = [
        ("TRATOR", "Trator" ),
        ("IMPLEMENTO AGRÍCOLA", "Implemento Agrícola" ),
    ]
    
    OPCOES_TEMA = [
        ("FRUTIFERAS", "Frutíferas" ),
        ("GRÃOES E FORRAGENS", "Grãos e Forragens" ),
        ("HORTICULTURA", "Horticultura" ),
        ("SOCIOBIODIVERSIDADE", "Sociobiodiversidade" ),
        ("TODAS", "Todas" ),
        ("OUTROS", "Outros" ),
    ]
    
    OPCOES_FUNCAO = [
        ("CONTROLE DE QUALIDADE", "Controle de Qualidade" ),
        ("PRODUTIVA", "Produtiva" ),
        ("TRATAMENTO DE RESIDUOS", "Tratamento de Resíduos" ),
        ("SEGURANCA E SAUDE DO TRABALHADOR", "Segurança e Saúde do Trabalhador" ),       
    ]
    
    OPCOES_ETAPA = [
        ("MANEJO", "Manejo" ),
        ("MANEJO-INDUSTRIALIZAÇÃO", "Manejo-Industrialização" ),
        ("PLANTIO", "Plantio" ),
        ("PREPARO DE SOLO", "Preparo de Solo" ),
        ("COLHEITA", "Colheita" ),
        ("PÓS-COLHEITA", "Pós-Colheita" ),
        ("INDUSTRIALIZAÇÃO", "Industrialização" ),
       
    ]
    
    OPCOES_NATUREZA = [
        ("TRATORES", "Tratores" ),
        ("PULVERIZADOR_AGRICOLA", "Pulverizador Agrícola" ),
        ("MÁQUINAS E APARELHOS PARA PREPARAÇÃO, TRABALHO DO SOLO OU CULTURA", "Máquinas e aparelhos para preparação, trabalho do solo ou cultura" ),
          
    ]
    
    OPCOES_FREQUENCIA_USO = [
        ("DESCONHECIDO", "Desconhecido" ),
        ("ESPORÁDICA", "Esporádica" ),
        ("DIÁRIA", "Diária" ),
        ("SEMANAL", "Semanal" ),
        ("MENSAL", "Mensal" ),
        ("TRIMESTRAL", "Trimestral" ),
        ("SEMESTRAL", "Semestral" ),
        ("ANUAL", "Anual" ),            
    ]
    
    TIPO_ITEM = [
        ("EQUIPAMENTO", "Equipamento" ),
        ("FERRAMENTA", "Ferramenta" ),
        ("INSTRUMENTO", "Instrumento" ),
        ("MAQUINA", "Máquina" ),
        ("VEICULO", "Veículo" ),
    ]
     
    
    foto = models.ImageField(null=True, upload_to="fotos/%Y/%m/%d/", blank=True)
    n = models.IntegerField(null=True, blank=True)
    codigo_catalogo = models.CharField(max_length=100, null=True, blank=True)
    codigo_questionario = models.CharField(max_length=100, null=True, blank=True)
    tema = models.CharField(null=True, max_length=100, choices=OPCOES_TEMA, default='')
    cadeia_produtiva = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(null=True, max_length=100, choices=TIPO_ITEM, default='')
    funcao = models.CharField(null=True, max_length=100, choices=OPCOES_FUNCAO, default='')
    etapa = models.CharField(null=True, max_length=100, choices=OPCOES_ETAPA, default='')
    sub_etapa_atividade = models.CharField(max_length=100, null=True, blank=True)
    utilizacao = models.CharField(max_length=500, null=True, blank=True)
    produto_linha_producao = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)     
    insumos_item = models.TextField(null=True, blank=True)   
    local_aquisicao_item = models.CharField(max_length=500, null=True, blank=True)
    ano_aquisicao_item = models.DateField(null=True, blank=True)
    caracteristicas_detalhadas_item = models.TextField(null=True, blank=True)
    codigo_finame = models.CharField(max_length=100, null=True, blank=True, default='') 
    fornecedor = models.ForeignKey(
        to=Fornecedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="fornecedor",
    )   
    aspectos_item_boas_praticas = models.TextField(null=True, blank=True)
    item_gera_residuo = models.BooleanField(null=True, default=False)
    qual_residuo = models.TextField(null=True, blank=True) 
    preco_min_item = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    preco_max_item = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    impacto_positivo_item = models.TextField(null=True, blank=True)
    condicoes_adequadas_uso = models.TextField(null=True, blank=True)
    tipo_uso_item = models.CharField(max_length=200, null=True, blank=True)
    qts_pessoas_usam = models.IntegerField(null=True, blank=True)
    faz_manutencao_item = models.BooleanField(null=True, default=False)
    frequencia_uso_item = models.CharField(null=True, max_length=100, choices=OPCOES_FREQUENCIA_USO, default='')
    problema_item_12_meses = models.CharField(max_length=200, null=True, blank=True)
    frequencia_manutencao_item_12_meses = models.CharField(max_length=200, null=True, blank=True)
    capacitacao_manutencao_item = models.BooleanField(null=True, default=False)
    tempo_uso_item_mes = models.CharField(max_length=200, null=True, blank=True)
    capacidade_producao_item = models.TextField(null=True, blank=True)  
    ncm = models.CharField(max_length=50, null=True, blank=True)
    ncm_descricao = models.TextField(null=True, blank=True) 
    estimativa_da_demanda = models.CharField(max_length=200, null=True, blank=True)    
    observacoes = models.TextField(null=True, blank=True)
    publicada = models.BooleanField(null=True, default=False)
    data_registro = models.DateTimeField(null=True, default=datetime.now, blank=True)
    
    modelo = models.CharField(max_length=100, null=True, blank=True)      
    linha_financiamento = models.TextField(null=True, blank=True)
    cnpj_fabricante = models.CharField(max_length=50, null=True, blank=True)
    nome_fabricante = models.CharField(max_length=100, null=True, blank=True)    
    natureza = models.TextField(null=True, choices=OPCOES_NATUREZA, blank=True)
    link_pagina = models.CharField(max_length=100, null=True, blank=True)    
    cultura = models.TextField(null=True, blank=True) 
    categoria = models.CharField(null=True, max_length=100, choices=OPCOES_CATEGORIA, default='') 
    operacao_agricola = models.CharField(null=True, blank=True)
    codigo_produto = models.CharField(max_length=100, null=True, blank=True)     
    hp = models.CharField(null=True, blank=True)     
        
    empresa = models.CharField(max_length=100, null=True, blank=True)
    
 
    def __str__(self):
        return self.nome
    
    
