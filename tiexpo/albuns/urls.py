from django.urls import path
from tiexpo.albuns import views

app_name = 'albuns'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('imagens/', views.imagens, name='imagens'),
    path('imagens/<slug:slug>', views.imagem, name='imagem'),
    path('', views.indice, name='indice'),
]
