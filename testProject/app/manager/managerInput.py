from app.models import *
import random

class ManagerInput:

    def addUser(self, name, email):
        try:
            user = Solicitante.objects.get(nombre=name)
            return user
        except Exception as e:
            print(e)
            new_solicitante = Solicitante(pk=uuid.uuid4(), nombre=name, correo=email)
            new_solicitante.save()
            return Solicitante.objects.get(nombre=name)

    def addProduct(self, product_name):
        try:
            prod = Producto.objects.get(nombre=product_name)
            return prod
        except Exception as e:
            print(e)
            marcas = Marca.objects.all()
            subcategorias = Subcategoria.objects.all()
            new_product = Producto(pk=uuid.uuid4(),
                                   nombre=product_name,
                                   marca=marcas[random.randint(0, 8)],
                                   subcategoria=subcategorias[random.randint(0, 8)],
                                   precio=random.randint(0, 100))
            new_product.save()
            return new_product

    def addSolcitud(self, products, solicitante):
        print('................')
        print(solicitante)
        print(products)
        new_solicitude = Solicitud()
        new_solicitude.save()
        str_amount = ''
        for product in products:
            new_solicitude.producto.add(product['prod'])
            str_amount = product['prod'].nombre + ':' + str(product['amount']) + ','
        new_solicitude.cantidad = str_amount
        new_solicitude.solicitante.add(solicitante)
        new_solicitude.save()
