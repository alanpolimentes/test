from app.models import *
from app.serializer.serializerA import ProductoSerializer
from django.forms.models import model_to_dict
from django.core.mail import send_mail


class manager:

    def __init__(self, id):
        self.id = id

    def calculateTotalSolicitud(self):
        try:
            solicitud = Solicitud.objects.get(pk=self.id)
        except Exception as e:
            print(e)
            return None
        products = solicitud.producto.all()
        solicitante = solicitud.solicitante.all()[0]
        dict_products = {'prods': {}, 'total': 0, 'user': {'correo': solicitante.correo, 'nombre': solicitante.nombre}}
        split_cantidad = solicitud.cantidad.split(',')
        key_val = {}
        for values in split_cantidad:
            if len(values) == 0:
                continue
            split_value = values.split(':')
            key_val[split_value[0]] = split_value[1]
        print(key_val)
        for product in products:
            if product.nombre not in dict_products['prods']:
                dict_products['prods'][product.nombre] = {}
                dict_products['prods'][product.nombre]['count'] = int(key_val[product.nombre])
                dict_products['prods'][product.nombre]['subtotal'] = int(key_val[product.nombre]) * product.precio
                dict_products['prods'][product.nombre]['subcategoria'] = product.subcategoria.nombre
                dict_products['prods'][product.nombre]['precio'] = product.precio
                dict_products['total'] = dict_products['total'] + dict_products['prods'][product.nombre]['subtotal']
        sendEmail(dict_products['user']['nombre'], dict_products['user']['correo'], dict_products['total'])
        return dict_products


def sendEmail(name, email, total):
    send_mail(
        'Email Django',
        'Gracias! ' + name + 'el costo es de ' + str(total),
        'testemaildjangopoli@gmail.com',
        ['testemaildjangopoli@gmail.com'],
    )

def getProductsbyCat():
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