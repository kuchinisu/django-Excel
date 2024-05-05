from rest_framework import serializers
from .models import GananicasTotalesHistorias, PasivoAPagar

class GananicasTotalesHistoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = GananicasTotalesHistorias
        fields = [
            'cantidad'
        ]

class PasivoAPagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasivoAPagar
        fields = [
            'nombre',
            'cantidad',
            'estado',
            'fecha_de_primer_pago',
            'por_tiempo',
            'ultima_fecha',
            'veces'
        ]