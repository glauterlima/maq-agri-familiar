from django.contrib import admin

from maqdisponivel.models import Maquina

class ListandoMaquinas(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "operacao_agricola", "tipo",
                    "cadeia_produtiva", "hp", "empresa", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome" ,)
    list_filter = ("categoria", )
    list_editable = ("publicada", )
    list_per_page = 10

admin.site.register(Maquina, ListandoMaquinas)
