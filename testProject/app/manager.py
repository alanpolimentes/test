from app.models import *
from app.serializer.serializerA import ProductoSerializer
from django.forms.models import model_to_dict


class manager:

    def __init__(self, id):
        self.id = id

    def calculateTotalSolicitud(self):
        solicitud = Solicitud(id=self.id)
        if Solicitud is None:
            return {}
        products = solicitud.producto.all()
        solicitante = solicitud.solicitante.all()[0]
        dict_products = {'prods': {}, 'total': 0, 'user': {'correo': solicitante.correo, 'nombre': solicitante.nombre}}

        for product in products:
            if product.nombre not in dict_products['prods']:
                dict_products['prods'][product.nombre] = {}
                dict_products['prods'][product.nombre]['count'] = 0
                dict_products['prods'][product.nombre]['subtotal'] = 0
                dict_products['prods'][product.nombre]['subcategoria'] = Producto_Subcat.objects.get(producto=product).subctegoria

            dict_products['prods'][product.nombre]['count'] = dict_products['prods'][product.nombre]['count'] + 1
            dict_products['prods'][product.nombre]['subtotal'] = dict_products['prods'][product.nombre]['subtotal'] + product.precio
            dict_products['total'] = dict_products['total'] + product.precio
        return dict_products


def getProductsbyCat():
    # Your_Model.objects.values('order_id', 'city', 'locality', 'login_time').order_by().annotate(sum('morning_hours'),
    #                                                                                             sum('afternoon_hours'),
    #                                                                                             sum('evening_hours'),
    #                                                                                             sum('total_hours'))
    all_products = Producto.objects.all()
    all_categories = Categoria.objects.all()
    dict_result = {}
    for product in all_products:
        categoria = product.subcategoria.categoria.nombre
        subcategoria = product.subcategoria.nombre
        marca = product.marca.nombre
        if categoria not in dict_result:
            dict_result[categoria] = {}
        if subcategoria not in dict_result[categoria]:
            dict_result[categoria][subcategoria] = {}
        if subcategoria not in dict_result[categoria][subcategoria]:
            dict_result[categoria][subcategoria][marca] = {}
        if product.nombre not in dict_result[categoria][subcategoria][marca]:
            dict_result[categoria][subcategoria][marca][product.nombre] = {'name': product.nombre}
    print(dict_result)

    return dict_result