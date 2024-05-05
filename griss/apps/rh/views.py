from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.utils.paginator import LargeSetPagination
from .models import Empleada, Socias
from .serializer import EmpleadaSerializer, SociasSerializer
from django.http import HttpResponse
import csv

class EmpleadasView(APIView):
    def get(self, request, format=None):
        empleadas = Empleada.objects.all()
        if not empleadas.exists():
            return Response({'error': 'No hay empleadas registradas.'}, status=status.HTTP_404_NOT_FOUND)

        if 'csv' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="empleadas.csv"'
            
            writer = csv.writer(response)
            writer.writerow(['Nombre', 'Salario'])  

            for empleada in empleadas:
                writer.writerow([empleada.nombre, empleada.salario])
            
            return response
        else:
            paginator = LargeSetPagination()
            result_page = paginator.paginate_queryset(empleadas, request)
            serializer = EmpleadaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

class SociasView(APIView):
    def get(self, request, format=None):
        if Socias.objects.all().exists():
            socias = Socias.objects.all()

            paginator = LargeSetPagination()
            result_page = paginator.paginate_queryset(socias, request)
            serializer = SociasSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)