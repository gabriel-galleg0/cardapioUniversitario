from decimal import Decimal
from django.contrib import admin
from django.db.models import Avg, Count, Q

class AmaralAdminSite(admin.AdminSite):
    site_header = "Amaral Cantina"
    site_title = "Administração | Amaral Cantina"
    index_title = "Visão geral do Cardápio"

    # Template personalizado da página inicial do Admin
    index_template = "admin/dashboard.html"

    # Mantém a navegação lateral do Django
    eneble_nav_sidebar = True
    
    def index(self, request, extra_context=None):
        # Imports internos para evitar problemas de importação circular
        from menu.models import Categoria, ItemCardapio

        total_produtos = ItemCardapio.objects.count()

        produtos_disponiveis = ItemCardapio.objects.filter(disponivel=True).count()

        produtos_indisponiveis = ItemCardapio.objects.filter(disponivel=False).count()

        total_categorias = Categoria.objects.count()

        preco_medio = ItemCardapio.objects.filter(disponivel=True).aggregate(
            media=Avg("preco")
        )["media"] or Decimal(0.00)

        if total_produtos:
            percentual_disponivel = round((produtos_disponiveis / total_produtos) * 100, 2)
        else:
            percentual_disponivel = 0.00

        categorias = list(
            Categoria.objects.annotate(
                total_itens=Count(
                    "itens",
                    distinct=True,
                ),
                itens_disponiveis=Count(
                    "itens",
                    filter=Q(itens__disponivel=True),
                    distinct=True,
                ),
            ).order_by(
                "-total_itens",
                "nome",
            )
        )

        categorias_sem_produtos = 0

        for categoria in categorias:
            if categoria.total_itens:
                categoria.percentual_disponivel = round(
                    categoria.itens_disponiveis / categoria.total_itens * 100)
            else:
                categoria.percentual_disponivel = 0
                categorias_sem_produtos += 1

        dashboard_context = {
            "total_produtos": total_produtos,
            "produtos_disponiveis": produtos_disponiveis,
            "produtos_indisponiveis": produtos_indisponiveis,
            "total_categorias": total_categorias,
            "categorias_sem_produtos": categorias_sem_produtos,
            "preco_medio": preco_medio,
            "percentual_disponivel": percentual_disponivel,
            "categorias_dashboard": categorias,
        }

        context = {
            **dashboard_context,
            **(extra_context or {}),
        }

        return super().index(request, extra_context=context)