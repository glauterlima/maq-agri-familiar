from django.db import models

class Fornecedor(models.Model):    
 
    cnpj = models.CharField(max_length=15, null=False, blank=False) 
    nome = models.CharField(max_length=100, null=False, blank=False) 
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
