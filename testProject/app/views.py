from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework import viewsets, status
from app.serializer.serializerA import *
from app.serializer.inputSerializer import *
from app.classTest.test import *
from app.manager.manager import *
from app.manager.managerInput import *
from app.errors import *
import random
import json
from django.http import Http404


class Hi(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='index.html')


class firstPetition(APIView):

    def get(self, request, *args, **kwargs):
        tem = test('A', 'B', 'C')
        value_ser = testSerializer(tem)
        print(value_ser.data)
        return Response(value_ser.data)


class allSolicitudes(viewsets.ViewSet):

    def get(self, request, *args, **kwargs):

        solicitudes = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitudes, many=True)

        return Response(serializer.data)


class specificSolicitude(viewsets.ViewSet):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        if id is None:
            raise Http404
        man = manager(id)
        calculated_data = man.calculateTotalSolicitud()
        if calculated_data is None:
            raise Http404
        serializer = ResponseSolicitudSerializer(data={'solicitud': calculated_data})
        serializer.is_valid()
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        man = manager(id)
        if id is None:
            raise Http404
        calculated_data = man.calculateTotalSolicitud()
        if calculated_data is None:
            raise Http404
        serializer = ResponseSolicitudSerializer(data={'solicitud': calculated_data})
        serializer.is_valid()
        return Response(serializer.data)


class AllProducts(viewsets.ViewSet):

    def get(self, request, *args, **kwargs):
        values = getProductsbyCat()
        serializer = ResponseGruopSerializer(data={'produtos': values})
        serializer.is_valid()
        return Response(serializer.data)


class addData(viewsets.ViewSet):

    def solicitud(self, request, *args, **kwargs):
        nombre = request.data.get('nombre')
        correo = request.data.get('correo')
        products_req = request.data.get('products')
        input = ManagerInput()
        list_products = []
        for key in products_req:
            tem_prod = input.addSemiRandProduct(key)
            list_products.append({'prod': tem_prod, 'amount': products_req[key]})
        solicitante = input.addUser(nombre, correo)
        input.addSolcitud(list_products, solicitante)

        return Response(status=status.HTTP_200_OK)

    def product(self, request, *args, **kwargs):
        try:
            serializer = InputProdSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                raise InvalidInput('Formato incorrecto', 'x')
        except InvalidInput as e:
            print(e, e.value)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)


class pushData(TemplateView):

    def get(self, request, *args, **kwargs):
        test_categorias = [
                {'name': 'salud', 'subcat': ['medicina', 'higiene']},
                {'name': 'alimentos', 'subcat': ['frituras', 'enlatado', 'natural']},
                {'name': 'electronicos', 'subcat': ['television', 'celulares', 'consolas']},
                {'name': 'ropa', 'subcat': ['pantalon', 'camisa', 'blusa']},
                {'name': 'autos', 'subcat': ['refacciones', 'enfriadores', 'accesorios']},
        ]
        test_values_marcas = ['marca1', 'marca2', 'marca3', 'marca4', 'marca5', 'marca6', 'marca7','marca9','marca10','marca11', ]
        test_values_solicitante = [{
            'nombre': 'usuario1',
            'correo': 'usuario1@correo.com'
        }, {
            'nombre': 'usuario2',
            'correo': 'usuario1@correo.com'
        }, {
            'nombre': 'usuario3',
            'correo': 'usuario1@correo.com'
        }]
        test_values_productos = [
            {'prod': 'jabon', 'sub': 'higiene', 'precio': 20},
            {'prod': 'jarabe', 'sub': 'medicina', 'precio': 200},
            {'prod': 'deshodorante', 'sub': 'higiene', 'precio': 25},
            {'prod': 'papas', 'sub': 'frituras', 'precio': 12},
            {'prod': 'llanta', 'sub': 'refacciones', 'precio': 600},
            {'prod': 'volante', 'sub': 'accesorios', 'precio': 600},
            {'prod': 'adorno', 'sub': 'accesorios', 'precio': 600},
            {'prod': 'sopa', 'sub': 'enlatado', 'precio': 8},
            {'prod': 'ps4', 'sub': 'consolas', 'precio': 8000},
            {'prod': 'xbox', 'sub': 'consolas', 'precio': 8000},
        ]

        dict_model_subcategorias = {}
        list_model_marcas = []
        list_model_productos = []
        for categoria in test_categorias:
            test_categorias = Categoria(id=uuid.uuid4(), nombre=categoria['name'])
            test_categorias.save()
            for sub in categoria['subcat']:
                test_subcategoria = Subcategoria(id=uuid.uuid4(), nombre=sub, categoria=test_categorias)
                test_subcategoria.save()
                # test_categorias.subcategoria.add(test_subcategoria)
                dict_model_subcategorias[sub] = test_subcategoria

        print('categorias ingresadas')
        print(dict_model_subcategorias)
        for marca in test_values_marcas:
            value_marca = Marca(id=uuid.uuid4(), nombre=marca)
            value_marca.save()
            print(value_marca)
            list_model_marcas.append(value_marca)
        print('marcas ingresadas')
        for prod in test_values_productos:
            index_marca = random.randint(0, 8)
            producto = Producto(
                id=uuid.uuid4(),
                nombre=prod['prod'],
                marca=list_model_marcas[index_marca],
                subcategoria=dict_model_subcategorias[prod['sub']],
                precio=prod['precio'],
            )
            producto.save()
            list_model_productos.append(producto)
        for sol in test_values_solicitante:
            solicitante = Solicitante(id=uuid.uuid4(), nombre=sol['nombre'], correo=sol['correo'])
            solicitante.save()
            solicitud = Solicitud(cantidad='8')
            solicitud.save()
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.producto.add(list_model_productos[random.randint(0, 8)])
            solicitud.solicitante.add(solicitante)
            str_cant = ''
            for product in solicitud.producto.all():
                str_cant = str_cant + product.nombre + ':' + str(random.randint(0, 5)) + ','
            solicitud.cantidad = str_cant
            solicitud.save()

        return render(request, template_name='index.html')