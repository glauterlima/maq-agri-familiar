from django.contrib import admin

from maqdesenvolvimento.models import MaqDesenvolvimento

class ListandoMaquinasEmDesenvolvimento(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "categoria")
    list_display_links = ("id", "nome")
    search_fields = ("nome" ,)
    list_filter = ("categoria", )
    list_per_page = 10

admin.site.register(MaqDesenvolvimento, ListandoMaquinasEmDesenvolvimento)

