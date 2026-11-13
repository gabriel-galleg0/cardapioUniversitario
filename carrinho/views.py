
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from uuid import uuid4

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST

from menu.models import ItemCardapio
from .cart import Carrinho


# ADICIONAR PRODUTO AO CARRINHO
@require_POST
def adicionar_ao_carrinho(request, item_id):
    carrinho = Carrinho(request)

    # Permite adicionar apenas produtos disponíveis
    item = get_object_or_404(
        ItemCardapio,
        id=item_id,
        disponivel=True
    )

    carrinho.adicionar(item)

    return redirect('/')


# REMOVER PRODUTO DO CARRINHO
@require_POST
def remover_do_carrinho(request, item_id):
    carrinho = Carrinho(request)

    item = get_object_or_404(
        ItemCardapio,
        id=item_id
    )

    carrinho.remover(item)

    return redirect('detalhe_carrinho')


# EXIBIR CARRINHO
def detalhe_carrinho(request):
    carrinho = Carrinho(request)

    return render(
        request,
        'carrinho/detalhe.html',
        {'carrinho': carrinho}
    )


# PÁGINA DE PAGAMENTO
def pagamento(request):
    carrinho = Carrinho(request)

    # Impede finalizar um carrinho vazio
    if not carrinho.carrinho:
        return redirect('/')

    return render(
        request,
        'carrinho/pagamento.html',
        {'carrinho': carrinho}
    )


# CONFIRMAR PEDIDO
@require_POST
def confirmar_pedido(request):
    carrinho = Carrinho(request)

    if not carrinho.carrinho:
        return redirect("/")

    itens_confirmados = []

    for item in carrinho:
        itens_confirmados.append({
            "nome": item["item"].nome,
            "quantidade": item["quantidade"],
            "preco_unitario": str(item["preco"]),
            "preco_total": str(item["preco_total"]),
        })

    pedido = {
        # Código temporário para o protótipo.
        # Em um sistema real, deve vir de um modelo Pedido.
        "codigo": uuid4().hex[:8].upper(),
        "itens": itens_confirmados,
        "total": str(carrinho.get_total()),
        "criado_em": timezone.localtime().strftime(
            "%d/%m/%Y às %H:%M"
        ),
    }

    request.session["pedido_confirmado"] = pedido

    carrinho.limpar()

    return redirect("pedido_confirmado")

# EXIBIR CONFIRMAÇÃO
def pedido_confirmado(request):
    pedido = request.session.get("pedido_confirmado")

    if not pedido:
        return redirect("/")

    return render(
        request,
        "carrinho/pedido_confirmado.html",
        {"pedido": pedido},
    )