import uuid
from django.db import models


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombre = models.CharField(max_length=50)


class Subcategoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombre = models.CharField(max_length=50)


class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, unique=False)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, unique=False)


class Solicitante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()


class Solicitud(models.Model):
    solicitante = models.ManyToManyField(Solicitante)
    producto = models.ManyToManyField(Producto)
    cantidad = models.CharField(max_length=100)
