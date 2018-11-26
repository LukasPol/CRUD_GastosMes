"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from contas.views import home, listagem, nova_transacao, update, delete

urlpatterns = [
    path('asd/', admin.site.urls),
    path('home', home),
    path('', listagem, name='url_list'),
    path('novo', nova_transacao, name='url_novo'),
    path('update/<int:pk>', update, name='url_update'), # para passar paramentros na urls
    path('delete/<int:pk>', delete, name='url_delete') 
]
