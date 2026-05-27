from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalhe_carrinho, name='detalhe_carrinho'),
    path('adicionar/<int:item_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('pagamento/', views.pagamento, name='pagamento'),
    path('confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
    path('confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
]