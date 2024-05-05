from django.db import models
import datetime

ESTADOS = (
    ('hecho','hecho'),
    ('en_espera','en_espera'),
    ('anulado', 'anulado'),
    ('finalizado','finalizado'),
    ('en_perioro','en_periodo'),
)
MODOS_DE_TIEMPO = (
    ('definido', 'definido'),
    ('indefinido', 'indefinido'),
    ('una_vez','una_vez'),
    ('cantidad_de_veces_definida', 'cantidad_de_veces_definida')
)
MODOS_DE_PERIODO_DE_PAGA = (
    ('semanal','semanal'),
    ('mensual','mensual'),
    ('quincenal','quincenal'),
    ('diario','diario'),
    ('anual','anual'),
    
)

class GananicasTotalesHistorias(models.Model):
    cantidad = models.DecimalField(default=0.00, max_digits=11, decimal_places=2)#999 999 999.99

class AactivoInmueble(models.Model):
    nombre = models.CharField(default='', max_length=50)

class ActivoMueble(models.Model):
    nombre = models.CharField(default='',max_length=50)

class DocumentosPorCobrar(models.Model):
    nombre = models.CharField(default='', max_length=255)
    cantidad = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    fecha_de_cobro = models.DateField(default=datetime.date.today())
    estado = models.CharField(default='en_espera', choices=ESTADOS, max_length=50)

class GastosTotalesHistorios(models.Model):
    cantidad = models.DecimalField(default=0.00, max_digits=11, decimal_places=2)#999 999 999.99

class PasivoAPagar(models.Model):
    nombre = models.CharField(default='', max_length=50)
    cantidad = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.CharField(default='en_perioro', choices=ESTADOS, max_length=50)
    fecha_de_primer_pago = models.DateField(default=datetime.date.today())
    por_tiempo = models.CharField(default='indefinido', max_length=50)
    ultima_fecha = models.DateField(default=datetime.date.today())
    veces = models.IntegerField(default=0)

class Adeudo(models.Model):
    cantidad_total = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    intereses = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    por_periodo = models.CharField(default='mensual', choices=MODOS_DE_PERIODO_DE_PAGA, max_length=50)
    estado = models.CharField(default='en_perioro', choices=ESTADOS, max_length=50)
    primer_pago = models.DateField(default=datetime.date.today())
    ultimo_pago = models.DateField(default=datetime.date.today())
    
class GastoImprevisto(models.Model):
    nombre = models.CharField(default='', max_length=100)
    cantidad = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    descripcion = models.TextField()