from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
 
from .serializer import GananicasTotalesHistoriasSerializer, PasivoAPagarSerializer
from apps.utils.paginator import SmallSetPagination
from .models import GananicasTotalesHistorias, PasivoAPagar

class GananciasTotalesHistoricasView(APIView):
    def get(self, request, format=None):
        if GananicasTotalesHistorias.objects.all().exists():            
            ganancias_totales_historias = GananicasTotalesHistorias.objects.all()

            paginator = SmallSetPagination()

            results = paginator.paginate_queryset(ganancias_totales_historias, request)
            serializer = GananicasTotalesHistoriasSerializer(results, many=True)
            return paginator.get_paginated_response({'gth':serializer.data})
        else:
            return Response({'error':'no se a empezado a contar las ganancias totales historias'},status=status.HTTP_404_NOT_FOUND)
class PasivosAPagarView(APIView):
    def get(self, request, format=None):
        if PasivoAPagar.objects.all().exists():
            pasivos = PasivoAPagar.objects.all()

            paginator = SmallSetPagination()

            results = paginator.paginate_queryset(pasivos, request)
            serializer = PasivoAPagarSerializer(results, many=True)
            return paginator.get_paginated_response({'pasivos':serializer.data})
        