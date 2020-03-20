from django.urls import path
from tiexpo.api import views

urlpatterns = [
    path('', views.album_list),
    path('imagens/', views.imagem_list),
    path('imagens/<int:id>/', views.imagem_detail),
]
