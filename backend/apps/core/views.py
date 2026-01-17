from django.http import HttpResponse

def pagina_inicial(request):
    return HttpResponse("Olá! Esta é a minha primeira rota no Django.")