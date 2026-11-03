
from django.contrib import admin
from .models import Categoria, ItemCardapio


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)
    ordering = ("nome",)
    list_per_page = 20


@admin.register(ItemCardapio)
class ItemCardapioAdmin(admin.ModelAdmin):

    # Colunas que aparecem na lista
    list_display = (
        "nome",
        "categoria",
        "preco",
        "disponivel",
    )

    # Filtros na lateral
    list_filter = (
        "categoria",
        "disponivel",
    )

    # Campo de pesquisa
    search_fields = (
        "nome",
        "descricao",
    )

    # Editar diretamente pela lista
    list_editable = (
        "preco",
        "disponivel",
    )

    # Ordenação dos produtos
    ordering = ("categoria__nome", "nome")

    # Quantidade por página
    list_per_page = 20
