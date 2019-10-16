import uuid
from django.db import models


class Subcategoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    subcategoria = models.ManyToManyField(Subcategoria, default=None)


class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)


class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.OneToOneField(Marca, on_delete=models.CASCADE)
    subcategoria = models.OneToOneField(Subcategoria, on_delete=models.CASCADE)


class Solicitante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()


class Solicitud(models.Model):
    solicitante = models.ManyToManyField(Solicitante)
    producto = models.ManyToManyField(Producto)