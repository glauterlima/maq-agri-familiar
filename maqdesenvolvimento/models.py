from django.db import models

class MaqDesenvolvimento(models.Model):
    
    OPCOES_CATEGORIA = [
        ("TRATOR", "Trator" ),
        ("IMPLEMENTO AGRÍCOLA", "Implemento Agrícola" ),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False) 
    descricao = models.TextField(null=False, blank=False) 
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='') 
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome