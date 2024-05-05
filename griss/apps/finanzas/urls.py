from django.urls import path
from .views import *

urlpatterns = [
    path('ganancias_totales_historicas/', GananciasTotalesHistoricasView.as_view()),
    path('pasivos_a_pagar/', PasivosAPagarView.as_view()),
]
