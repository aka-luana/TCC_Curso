"""medfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.views.static import serve

from django.conf.urls.static import static
from django.conf import settings
from django.template.response import TemplateResponse 

urlpatterns = [
    path('', include('AvaliacaoDiaria.urls')),
    path('', include('Perfil.urls')),
    path('', include('Medicacao.urls')),
    path('', include('Sangue.urls')),
    path('', include('Vacinas.urls')),
    path('', include('CadastroDePessoa.urls')),
    path('', include('Cirurgias.urls')),
    path('', include('DoencasExistentes.urls')),
    path('', include('Historico.urls')),
    path('', include('Cirurgias.urls')),
    path('accounts/', include('Accounts.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^', TemplateResponse, {'template': '404.html'}))