from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context


def inicio(request):
    return HttpResponse('Hola soy mi primer vista en django')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha_actual}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')
    # return HttpResponse(f'<h1>Hola {nombre}</h1>')
    
def mi_template(request):
    
    archivo = open(r'C:\Source Code\Coder\31085\DjangoClases\templates\prueba.html', 'r')
    
    template1 = Template(archivo.read())
    
    archivo.close()
    
    contexto1 = Context()
    
    render1 = template1.render(contexto1)
    
    return HttpResponse(render1)