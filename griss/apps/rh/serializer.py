from rest_framework import serializers
from .models import Empleada, Socias
class EmpleadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleada
        fields = [
            'numero',
            'nombre',
            'nombre',
            'apellido_materno',
            'apellido_paterno',
            'fecha_de_nacimiento',
            'salario',
            'fecha_de_primer_paga',
            'modo_periodo_de_paga',
            'fecha_de_entrada',
        ]
class SociasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socias
        fields = [
            'nombre',
            'apellido_materno',
            'apellido_paterno',
            'aportado',
            'participacion',
            'ganancias_totales_historicas',
        ]
