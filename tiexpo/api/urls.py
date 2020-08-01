from django.urls import path
from tiexpo.api import views

urlpatterns = [
    path('', views.ImageList.as_view()),
    path('imagens/', views.ImageApiView.as_view()),
    path('imagens/<int:pk>/', views.ImageDetail.as_view()),
    path('imagens/catalogos/', views.CatalogoList.as_view()),
]
