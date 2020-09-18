from django.urls import path

from tiexpo.base.views import home, privacy


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('privacidade/', privacy, name='privacy'),
]
