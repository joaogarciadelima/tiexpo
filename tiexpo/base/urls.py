from django.urls import path
from django.views.generic import TemplateView

from tiexpo.base.views import home


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('service_worker.js', (
        TemplateView.as_view(
            template_name="base/service_worker.js",
            content_type='application/javascript', )), name='service_worker.js'),
]
