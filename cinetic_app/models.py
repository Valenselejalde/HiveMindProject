from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, null=True)
    token = models.CharField(max_length=100, default='', null=True, blank=True)

class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=20)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    idioma = models.CharField(max_length=20)

class Proyeccion(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    fecha_inicio = models.DateTimeField(auto_now=False)
    formato = models.CharField(max_length=20)

class Silla(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    fila = models.CharField(max_length=2)
    columna = models.CharField(max_length=2)
    tipo = models.CharField(max_length=20)
    precio = models.IntegerField()

class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now=True)

class Boleta(models.Model):
    proyeccion = models.ForeignKey(Proyeccion, on_delete=models.PROTECT)
    silla = models.ForeignKey(Silla, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=20)
    precio = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)

class Producto(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=20)
    precio_unitario = models.IntegerField()
    cantidad_inventario = models.IntegerField()

class Combo(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=20)
    porcentaje_descuento = models.IntegerField()
    productos = models.ManyToManyField('Producto', through='ProductoCombo')

class ProductoCombo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    cantidad_unidades = models.IntegerField()

class DetalleOrden(models.Model):
     producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
     combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
     cantidad = models.IntegerField()
     precio = models.IntegerField()
     venta = models.ForeignKey(Venta, on_delete=models.PROTECT)