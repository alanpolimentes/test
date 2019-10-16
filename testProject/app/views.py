from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework.views import APIView
from app.serializer.serializerA import *
from app.classTest.test import *
from rest_framework import viewsets


class Hi(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')


class firstPetition(APIView):

    def get(self, request, *args, **kwargs):
        tem = test('A', 'B', 'C')
        value_ser = testSerializer(tem)
        print(value_ser.data)
        return Response(value_ser.data)


