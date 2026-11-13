from django.db import models

from menu.models import ItemCardapio

# Create your models here.
class Pedido(models.Model):
    class Status(models.TextChoices):
        PENDENTE = "pendente", "Pendente"
        PAGO = "pago", "Pago"
        EM_PREPARO = "em_preparo", "Em preparo"
        PRONTO = "pronto", "Pronto"
        ENTREGUE = "entregue", "Entregue"
        CANCELADO = "cancelado", "Cancelado"

    numero = models.PositiveIntegerField(unique=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDENTE,
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento_id = models.CharField(max_length=150, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        related_name="itens",
        on_delete=models.CASCADE,
    )
    item_cardapio = models.ForeignKey(
        ItemCardapio,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    nome = models.CharField(max_length=100)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()