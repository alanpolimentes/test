from rest_framework import serializers
from app.models import *


class testSerializer(serializers.Serializer):
    fieldA = serializers.CharField()
    fieldB = serializers.CharField()
    fieldC = serializers.CharField()


class ProductoSerializer(serializers.ModelSerializer):
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