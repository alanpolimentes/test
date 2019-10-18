from rest_framework import serializers
from app.models import *


class testSerializer(serializers.Serializer):
    fieldA = serializers.CharField()
    fieldB = serializers.CharField()
    fieldC = serializers.CharField()


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombre']


class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Subcategoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    subcategoria = SubcategoriaSerializer()

    class Meta:
        model = Producto
        fields = '__all__'


class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = '__all__'


class SolicitudSerializer(serializers.ModelSerializer):
    solicitante = SolicitanteSerializer(many=True)
    producto = ProductoSerializer(many=True)

    class Meta:
        model = Solicitud
        fields = '__all__'


class ResponseSolicitudSerializer(serializers.Serializer):
    solicitud = serializers.DictField()

    class Meta:
        fields = '__all__'


class ResponseGruopSerializer(serializers.Serializer):
    produtos = serializers.DictField()

    class Meta:
        fields = '__all__'