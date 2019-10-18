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

    def addSemiRandProduct(self, product_name):
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

    def addMarca(self, marca_name):
        try:
            marca = Marca.objects.get(nombre=marca_name)
            return marca
        except Exception as e:
            print(e)
            new_marca = Marca(pk=uuid.uuid4(), nombre=marca_name)
            new_marca.save()
            return new_marca

    def addSubcategoria(self, subcategoria_name, categoria):
        try:
            subcategoria = Subcategoria.objects.get(nombre=subcategoria_name)
            return subcategoria
        except Exception as e:
            print(e)
            new_subcat = Subcategoria(pk=uuid.uuid4(), nombre=subcategoria_name, categoria=categoria)
            new_subcat.save()
            return new_subcat

    def addCategoria(self, categoria_name):
        try:
            subcategoria = Categoria.objects.get(nombre=categoria_name)
            return subcategoria
        except Exception as e:
            print(e)
            new_cat = Categoria(pk=uuid.uuid4(), nombre=categoria_name)
            new_cat.save()
            return new_cat

    def addCompleteProduct(self, categoria_name, subcategoria_name, marca_name, product_name, precio):
        try:
            product = Producto.objects.get(nombre=product_name)
            return product
        except Exception as e:
            print(e)
            categoria = self.addCategoria(categoria_name)
            subcategoria = self.addSubcategoria(subcategoria_name, categoria)
            marca = self.addMarca(marca_name)
            new_product = Producto(pk=uuid.uuid4(),
                                   nombre=product_name,
                                   subcategoria=subcategoria,
                                   marca=marca,
                                   precio=precio)
            new_product.save()
            return new_product

    def addSolcitud(self, products_req, nombre_sol, correo_sol):
        solicitante = self.addUser(nombre_sol, correo_sol)
        list_products = []
        for key in products_req:
            tem_prod = self.addSemiRandProduct(key)
            list_products.append({'prod': tem_prod, 'amount': products_req[key]})
        new_solicitude = Solicitud()
        new_solicitude.save()
        str_amount = ''
        for product in list_products:
            new_solicitude.producto.add(product['prod'])
            str_amount = product['prod'].nombre + ':' + str(product['amount']) + ','
        new_solicitude.cantidad = str_amount
        new_solicitude.solicitante.add(solicitante)
        new_solicitude.save()
        return new_solicitude
