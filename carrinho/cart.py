# carrinho/cart.py
from decimal import Decimal
from menu.models import ItemCardapio  # usa o modelo dos itens do cardápio

class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho')
        if not carrinho:
            carrinho = self.session['carrinho'] = {}
        self.carrinho = carrinho

    def adicionar(self, item, quantidade=1):
        item_id = str(item.id)
        if item_id not in self.carrinho:
            self.carrinho[item_id] = {
                'quantidade': 0,
                'preco': str(item.preco)
            }
        self.carrinho[item_id]['quantidade'] += quantidade
        self.salvar()

    def remover(self, item):
        item_id = str(item.id)
        if item_id in self.carrinho:
            del self.carrinho[item_id]
            self.salvar()

    def salvar(self):
        self.session.modified = True

    def limpar(self):
        self.session['carrinho'] = {}
        self.session.modified = True

    def __iter__(self):
        item_ids = self.carrinho.keys()
        itens = ItemCardapio.objects.filter(id__in=item_ids)
        for item in itens:
            carrinho_item = self.carrinho[str(item.id)]
            carrinho_item['item'] = item
            carrinho_item['preco_total'] = Decimal(carrinho_item['preco']) * carrinho_item['quantidade']
            yield carrinho_item

    def get_total(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item in self.carrinho.values())
