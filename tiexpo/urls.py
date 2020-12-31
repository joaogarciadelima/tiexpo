"""controledental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetCompleteView, PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from tiexpo.api.views import CustomAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/login/', LoginView.as_view(), name='login'),
    path('contas/logout/', LogoutView.as_view(), name='logout'),
    path('contas/reiniciar_senha/', PasswordResetView.as_view(), name='password_reset'),
    path('contas/reiniciar_senha/ok', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('contas/reiniciar/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('contas/reiniciar/ok', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('tiexpo.base.urls')),
    path('catalogos/', include('tiexpo.catalogos.urls'), name='albuns'),
    path('api/v1/', include('tiexpo.api.urls'), name='api'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth')

]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
