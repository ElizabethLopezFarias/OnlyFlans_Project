"""
URL configuration for proyecto_onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from web.views import indice, acerca, bienvenido, contacto, exito_contacto, cerrar_sesion, iniciar_sesion, hacer_pedido, pagina_de_confirmacion, hacer_pedido_premium
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name="indice"),
    path('acerca/', acerca, name="acerca"),
    path('bienvenido/', bienvenido, name="bienvenido"),
    path('contacto/', contacto, name="contacto"),
    path('exito_contacto/', exito_contacto, name="exito"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('hacer_pedido/', hacer_pedido, name='hacer_pedido'),
    path('hacer_pedido_premium/', hacer_pedido_premium, name='hacer_pedido_premium'),
    path('pagina_de_confirmacion/', pagina_de_confirmacion, name='pagina_de_confirmacion'),
]
