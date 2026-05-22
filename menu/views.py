from django.shortcuts import render
from .models import Categoria

def cardapio(request):
    categorias = Categoria.objects.prefetch_related("itens").all()
    return render(request, "cardapio.html", {"categorias": categorias})
