from app.models import *


class manager:

    def __init__(self, id):
        self.id = id

    def calculateTotalSolicitud(self):
        solicitud = Solicitud(id=self.id)
        if Solicitud is None:
            return -1
        products = solicitud.producto.all()
        dict_products = {}
        for product in products:
            if product.nombre not in dict_products:
                dict_products[product.nombre] = {}
                dict_products[product.nombre]['count'] = 0
                dict_products[product.nombre]['subtotal'] = 0
            dict_products[product.nombre]['count'] = dict_products[product.nombre]['count'] + 1
            dict_products[product.nombre]['subtotal'] = dict_products[product.nombre]['subtotal'] + product.precio

        return dict_products