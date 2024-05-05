from django.db import models
import datetime
from apps.inventario.models import Producto

ESTADOS_DE_PEDIDO = (
    ('en_proceso','en_proceso'),
    ('entregado', 'entregado'),
    ('cancelado','cancelado'),
    ('devuelto','devuelto'),
)

TIPOS_DE_PEDIDO = (
    ('producto_del_inventario','productos_del_inventario'),
    ('productos_por_encargo','productos_por_encargo'),
)

class Pedido(models.Model):
    fecha_de_entrega = models.DateField(default=datetime.date.today())
    fecha_de_pedido = models.DateField(default=datetime.date.today())
    tipo_de_pedido = models.CharField(default='producto_del_inventario', choices=TIPOS_DE_PEDIDO, max_length=23)
    lugar_de_entrega = models.CharField(default='en_tienda', max_length=255)
    
    productos = models.ManyToManyField(Producto, related_name='pedidos')
    nombre_del_cliente = models.CharField(default='####', max_length=255)
    numero_de_telefono = models.CharField(default='##########', max_length=8)
    def __str__(self):
        return str(f'pedido del {self.fecha_de_pedido} para el {self.fecha_de_entrega} a {self.lugar_de_entrega} para el cliente {self.nombre_del_cliente}')


    