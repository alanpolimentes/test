from app.models import *


class manager:

    def __init__(self, id):
        self.id = id

    def calculateTotalSolicitud(self):
        solicitud = Solicitud(id=self.id)
        if Solicitud is None:
            return -1
        products = solicitud.producto.all()
        dict_products = {'prods': {}, 'total': 0}

        for product in products:
            if product.nombre not in dict_products['prods']:
                dict_products['prods'][product.nombre] = {}
                dict_products['prods'][product.nombre]['count'] = 0
                dict_products['prods'][product.nombre]['subtotal'] = 0
            dict_products['prods'][product.nombre]['count'] = dict_products['prods'][product.nombre]['count'] + 1
            dict_products['prods'][product.nombre]['subtotal'] = dict_products['prods'][product.nombre]['subtotal'] + product.precio
            dict_products['total'] = dict_products['total'] + product.precio
        return dict_products


class ResponseData:
    def __init__(self, products, total):
        self.products = products
        self.total = total
