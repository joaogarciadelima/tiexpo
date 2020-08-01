from django.urls import path
from tiexpo.api import views

urlpatterns = [
    path('', views.CatalogoList.as_view()),
    path('imagens/', views.ImageList.as_view()),
    path('imagens/<int:pk>/', views.ImageDetail.as_view()),
    path('imagens/catalogos/', views.CatalogoList.as_view()),
    # path('imagens/catalogos/<int:catalogo_id>', views.highlight),
]
