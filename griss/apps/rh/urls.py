from django.urls import path
from .views import *

urlpatterns = [
    path('lista_de_empleadas/', EmpleadasView.as_view()),
    path('lista_de_socias/', SociasView.as_view()),
]
