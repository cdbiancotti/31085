from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context, loader

from primerasvistas.models import Perro


def inicio(request):
    return HttpResponse('Hola soy mi primer vista en django')


def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha_actual}')


def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')
    # return HttpResponse(f'<h1>Hola {nombre}</h1>')

# v1
# def mi_template(request):

#     archivo = open(
#         r'C:\Source Code\Coder\31085\DjangoClases\templates\prueba.html', 'r')

#     template1 = Template(archivo.read())

#     archivo.close()

#     nombre = 'Momia'

#     contexto1 = Context({'nombre': nombre})

#     render1 = template1.render(contexto1)

#     return HttpResponse(render1)


# v2
def mi_template(request, nombre_perro, edad_perro):

    template1 = loader.get_template('prueba.html')

    nombre = 'Momia'
    apellido = 'Blanca'

    lista = ['Ricardo', 'Pepe', 'Franco',
             'Cristian', 'Artemis', 'Zeus', 'Felix']

    perro = Perro(nombre=nombre_perro, edad=edad_perro)
    perro.save()

    render1 = template1.render(
        {'nombre': nombre, 'apellido': apellido, 'edad': 6000, 'lista': lista, 'perro': perro})

    return HttpResponse(render1)


def listado_perros(request):

    template = loader.get_template('listado_perros.html')

    lista_perros = Perro.objects.all()

    render = template.render({'lista_perros': lista_perros})

    return HttpResponse(render)
