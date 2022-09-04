from dataclasses import fields
from rest_framework import serializers
from cinetic_app.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
    def create(self, validated_data):
        user = Usuario(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            telefono = validated_data['telefono'],
            direccion = validated_data['direccion'],
            fecha_nacimiento = validated_data['fecha_nacimiento']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class ProyeccionSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    pelicula = PeliculaSerializer(read_only=True)
    pelicula_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all(), source='pelicula')
    class Meta:
        model = Proyeccion
        fields = '__all__'

class SillaSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    class Meta:
        model = Silla
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Usuario.objects.all(), source='usuario')
    class Meta:
        model = Venta
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    proyeccion = ProyeccionSerializer(read_only=True)
    proyeccion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Proyeccion.objects.all(), source='proyeccion')
    silla = SillaSerializer(read_only=True)
    silla_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Silla.objects.all(), source='silla')
    venta = VentaSerializer(read_only=True)
    venta_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Venta.objects.all(), source='venta')
    class Meta:
        model = Boleta
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    class Meta:
        model = Producto
        fields = '__all__'

class ComboSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')
    class Meta:
        model = Combo
        fields = '__all__'

class ProductoComboSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = ComboSerializer(read_only=True)
    combo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    class Meta:
        model = ProductoCombo
        fields = '__all__'

class DetalleOrdenSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')
    combo = ComboSerializer(read_only=True)
    combo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')
    venta = VentaSerializer(read_only=True)
    venta_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Venta.objects.all(), source='venta')
    class Meta:
        model = DetalleOrden
        fields = '__all__'

