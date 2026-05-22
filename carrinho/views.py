from django.shortcuts import render, redirect, get_object_or_404
from menu.models import ItemCardapio
from .cart import Carrinho

def adicionar_ao_carrinho(request, item_id):
    carrinho = Carrinho(request)
    item = get_object_or_404(ItemCardapio, id=item_id)
    carrinho.adicionar(item)
    return redirect('/')

def remover_do_carrinho(request, item_id):
    carrinho = Carrinho(request)
    item = get_object_or_404(ItemCardapio, id=item_id)
    carrinho.remover(item)
    return redirect('detalhe_carrinho')

def detalhe_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho/detalhe.html', {'carrinho': carrinho})
