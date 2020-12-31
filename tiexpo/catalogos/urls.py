from django.urls import path
from tiexpo.catalogos import views

app_name = 'catalogos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('imagens/', views.imagens, name='imagens'),
    path('imagens/lancamentos/', views.imagens_destaques, name='destaques'),
    path('imagens/<slug:slug>', views.imagem, name='imagem'),
    path('imagens/like/<slug:slug>', views.new_like, name='new_like'),
    path('', views.indice, name='indice'),
    path('search/', views.procurar_imagens, name='search'),
    path('fabricantes/<slug:slug>', views.detalhe_fabricante, name='fabricantes'),
    path('fabricantes/', views.indice_fabricantes, name='indice_fabricantes'),
]
