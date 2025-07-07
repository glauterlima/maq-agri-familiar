from django.db import models

class Fornecedor(models.Model): 
    
    OPCOES_UF = [
        ("AC", "AC" ),
        ("AL", "AL" ),
        ("AP", "AP" ),
        ("AM", "AM" ),
        ("BA", "BA" ),
        ("CE", "CE" ),
        ("DF", "DF" ),
        ("ES", "ES" ),
        ("GO", "GO" ),
        ("MA", "MA" ),
        ("MT", "MT" ),
        ("MS", "MS" ),
        ("MG", "MG" ),
        ("PA", "PA" ),
        ("PB", "PB" ),
        ("PR", "PR" ),
        ("PE", "PE" ),
        ("PI", "PI" ),
        ("RJ", "RJ" ),
        ("RN", "RN" ),
        ("RS", "RS" ),
        ("RO", "RO" ),
        ("RR", "RR" ),
        ("SC", "SC" ),
        ("SP", "SP" ),
        ("SE", "SE" ),
        ("TO", "TO" ),
    ]   
 
    cnpj = models.CharField(max_length=30, null=False, blank=False, unique=True) 
    nome = models.CharField(max_length=100, null=False, blank=False) 
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)    
    logradouro = models.CharField(max_length=100, null=False, blank=False, default='') 
    cidade = models.CharField(max_length=100, null=False, blank=False, default='') 
    uf = models.CharField(null=True, max_length=2, choices=OPCOES_UF, default='')
    telefone = models.CharField(max_length=12, null=False, blank=False, default='')
    email = models.CharField(max_length=100, null=False, blank=False, default='')
    site = models.CharField(max_length=100, null=False, blank=False, default='')
    ativo = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nome
