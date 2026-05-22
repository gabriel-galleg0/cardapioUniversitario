from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalhe_carrinho, name='detalhe_carrinho'),
    path('adicionar/<int:item_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
