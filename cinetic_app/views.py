from django.shortcuts import render
from cinetic_app.models import *
from cinetic_app.serializers import *
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        # if not created:
        #     token.delete()
        
        # token, created = Token.objects.get_or_create(user=user)

        user.token = token.key
        user.save()
        usuario = UsuarioSerializer(user)
        
        return Response(usuario.data)

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class SalaView(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class PeliculaView(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class ProyeccionView(viewsets.ModelViewSet):
    queryset = Proyeccion.objects.all()
    serializer_class = ProyeccionSerializer

class SillaView(viewsets.ModelViewSet):
    queryset = Silla.objects.all()
    serializer_class = SillaSerializer

class VentaView(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class BoletaView(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ComboView(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer

class ProductoComboView(viewsets.ModelViewSet):
    queryset = ProductoCombo.objects.all()
    serializer_class = ProductoComboSerializer

class DetalleOrdenView(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer