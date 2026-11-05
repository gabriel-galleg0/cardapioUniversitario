from django.contrib import admin, messages
from django.db.models import Count

from .models import Categoria, ItemCardapio


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "total_itens",
    )

    search_fields = (
        "nome",
    )

    ordering = (
        "nome",
    )

    list_per_page = 20

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        return queryset.annotate(
            quantidade_itens=Count(
                "itens",
                distinct=True,
            )
        )

    @admin.display(
        description="Itens",
        ordering="quantidade_itens",
    )
    def total_itens(self, obj):
        return obj.quantidade_itens


@admin.register(ItemCardapio)
class ItemCardapioAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "categoria",
        "preco",
        "disponivel",
    )

    list_display_links = (
        "nome",
    )

    list_filter = (
        "categoria",
        "disponivel",
    )

    search_fields = (
        "nome",
        "descricao",
        "categoria__nome",
    )

    list_editable = (
        "preco",
        "disponivel",
    )

    ordering = (
        "categoria__nome",
        "nome",
    )

    list_select_related = (
        "categoria",
    )

    autocomplete_fields = (
        "categoria",
    )

    list_per_page = 20
    save_on_top = True

    fieldsets = (
        (
            "Produto",
            {
                "fields": (
                    "nome",
                    "descricao",
                    "categoria",
                )
            },
        ),
        (
            "Venda",
            {
                "fields": (
                    "preco",
                    "disponivel",
                )
            },
        ),
        (
            "Imagem",
            {
                "fields": (
                    "imagem",
                )
            },
        ),
    )

    actions = (
        "marcar_como_disponivel",
        "marcar_como_indisponivel",
    )

    @admin.action(
        description="Marcar selecionados como disponíveis"
    )
    def marcar_como_disponivel(
        self,
        request,
        queryset,
    ):
        atualizados = queryset.update(
            disponivel=True
        )

        self.message_user(
            request,
            (
                f"{atualizados} produto(s) "
                "marcado(s) como disponível(is)."
            ),
            level=messages.SUCCESS,
        )

    @admin.action(
        description="Marcar selecionados como indisponíveis"
    )
    def marcar_como_indisponivel(
        self,
        request,
        queryset,
    ):
        atualizados = queryset.update(
            disponivel=False
        )

        self.message_user(
            request,
            (
                f"{atualizados} produto(s) "
                "marcado(s) como indisponível(is)."
            ),
            level=messages.SUCCESS,
        )