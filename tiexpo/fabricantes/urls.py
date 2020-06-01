from django.urls import path
from tiexpo.fabricantes import views

app_name = 'fabricantes'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('', views.indice, name='indice'),
]
