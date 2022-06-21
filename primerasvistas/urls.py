from django.urls import path
from .views import inicio, ver_fecha, saludo, mi_template, listado_perros

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('saludo/<nombre>/', saludo),
    path('mi-template/<nombre_perro>/<edad_perro>/', mi_template),
    path('listado-perros/', listado_perros),
]
