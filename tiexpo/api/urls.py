from django.urls import path
from tiexpo.api import views

urlpatterns = [
    path('', views.catalogo_list),
    path('imagens/', views.imagem_list),
    path('imagens/<int:id>/', views.imagem_detail),
    # path('imagens/catalogos/<str: titulo>', views.catalogo_imagens_list),
    # path('imagens/fabricantes/', views.imagem_detail),
]
