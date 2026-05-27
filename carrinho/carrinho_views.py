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

def pagamento(request):
    carrinho = Carrinho(request)
    # Se o carrinho estiver vazio, manda de volta pro cardápio
    if not carrinho.carrinho:
        return redirect('/')
    return render(request, 'carrinho/pagamento.html', {'carrinho': carrinho})

def confirmar_pedido(request):
    if request.method != 'POST':
        return redirect('pagamento')
    carrinho = Carrinho(request)
    if not carrinho.carrinho:
        return redirect('/')
    # Salva os itens na sessão antes de limpar, para exibir na tela de confirmação
    itens_confirmados = []
    for item in carrinho:
        itens_confirmados.append({
            'nome': item['item'].nome,
            'quantidade': item['quantidade'],
            'preco_total': str(item['preco_total']),
        })
    total = str(carrinho.get_total())
    request.session['pedido_confirmado'] = {
        'itens': itens_confirmados,
        'total': total,
    }
    carrinho.limpar()
    return redirect('pedido_confirmado')

def pedido_confirmado(request):
    pedido = request.session.get('pedido_confirmado')
    if not pedido:
        return redirect('/')
    # Limpa da sessão para não reaparecer se o usuário atualizar
    del request.session['pedido_confirmado']
    request.session.modified = True
    return render(request, 'carrinho/pedido_confirmado.html', {'pedido': pedido})
