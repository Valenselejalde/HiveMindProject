"""cinetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from cinetic_app.views import *

router = routers.DefaultRouter()
router.register('usuario', UsuarioView, basename='usuario')
router.register('sala', SalaView, basename='sala')
router.register('pelicula', PeliculaView, basename='pelicula')
router.register('proyeccion', ProyeccionView, basename='proyeccion')
router.register('silla', SillaView, basename='silla')
router.register('venta', VentaView, basename='venta')
router.register('boleta', BoletaView, basename='boleta')
router.register('producto', ProductoView, basename='producto')
router.register('combo', ComboView, basename='combo')
router.register('productocombo', ProductoComboView, basename='productocombo')
router.register('detalleorden', DetalleOrdenView, basename='detalleorden')

urlpatterns = [
    path('', include(router.urls)),
    path('token', LoginView.as_view(), name='token')
]