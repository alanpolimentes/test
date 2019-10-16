from rest_framework import serializers


class testSerializer(serializers.Serializer):
    fieldA = serializers.CharField()
    fieldB = serializers.CharField()
    fieldC = serializers.CharField()

