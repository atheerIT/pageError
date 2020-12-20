from django.shortcuts import render
import socket
from django.http import JsonResponse, HttpResponse, HttpRequest


# Create your views here.
def index(request):
    return render(request, 'localPage/index.html')

def info(request):
    add= request.META['REMOTE_ADDR']
    name = socket.getfqdn(add)
    return JsonResponse({
        'add': add,
        'name': name,
    })

    