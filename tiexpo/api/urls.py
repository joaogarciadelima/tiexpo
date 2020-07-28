from django.urls import path
from tiexpo.api import views

urlpatterns = [
    path('', views.catalogo_list),
    path('imagens/', views.imagem_list),
    path('imagens/<int:id>/', views.imagem_detail),
    path('imagens/catalogos/', views.catalogo_list),
    # path('imagens/fabricantes/', views.imagem_detail),
]
