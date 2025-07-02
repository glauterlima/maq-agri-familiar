from django.contrib import admin

from apps.fornecedores.models import Fornecedor

class ListandoFornecedores(admin.ModelAdmin):
    list_display = ("id", "cnpj", "nome", "ativo")
    list_display_links = ("id", "nome")
    search_fields = ("nome" ,)
    list_editable = ("ativo", )
    list_per_page = 10

admin.site.register(Fornecedor, ListandoFornecedores)
