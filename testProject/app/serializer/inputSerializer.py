from rest_framework import serializers
from app.manager.managerInput import *
from app.models import *


class InputProdSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    categoria = serializers.CharField()
    subcategoria = serializers.CharField()
    marca = serializers.CharField()
    precio = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        input = ManagerInput()
        return input.addCompleteProduct(validated_data['categoria'], validated_data['subcategoria'], validated_data['marca'], validated_data['nombre'], validated_data['precio'])


class InputSolicitudSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    correo = serializers.CharField()
    products = serializers.DictField()

    def create(self, validated_data):
        print(validated_data)
        input = ManagerInput()
        return input.addSolcitud(validated_data['products'], validated_data['nombre'], validated_data['correo'])