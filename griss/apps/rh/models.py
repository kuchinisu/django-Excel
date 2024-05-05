from typing import Any
from django.db import models
import datetime

MODOS_DE_PERIODO_DE_PAGA = (
    ('semanal','semanal'),
    ('quincenal','quincenal'),
    ('diario','diario'),
    ('anual','anual'),
)
class Empleada(models.Model):
    numero = models.IntegerField(default=1)
    nombre = models.CharField(default='', max_length=100)
    apellido_materno = models.CharField(default='', max_length=100)
    apellido_paterno = models.CharField(default='', max_length=100)
    fecha_de_nacimiento = models.DateField(default=datetime.date.today())
    salario = models.DecimalField(default=248.98, max_digits=9, decimal_places=2)
    fecha_de_primer_paga = models.DateField(default=datetime.date.today())
    modo_periodo_de_paga = models.CharField(default='semanal', choices=MODOS_DE_PERIODO_DE_PAGA, max_length=50)
    fecha_de_entrada = models.DateField(default=datetime.date.today())
    def __str__(self):
        if self.nombre and self.apellido_materno and self.apellido_paterno:
            return str(f'{self.apellido_paterno} {self.apellido_materno} {self.nombre}')
        return 'empleada #####'
    def get_nombre(self):
        if self.nombre and self.apellido_materno and self.apellido_paterno:
            return str(f'{self.apellido_paterno} {self.apellido_materno} {self.nombre}')
        return 'empleada #####'
class GaffetDeEmpleada(models.Model):
    empleada = models.ForeignKey(Empleada, on_delete=models.CASCADE)
    def __init__(self):
        if self.empleada:
            return self.empleada.get_nombre()
        return 'empleada #####'
    
class Socias(models.Model):
    nombre = models.CharField(default='', max_length=100)
    apellido_materno = models.CharField(default='', max_length=100)
    apellido_paterno = models.CharField(default='', max_length=100)
    aportado = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    participacion = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    ganancias_totales_historicas = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    def __str__(self):
        return str(self.nombre)