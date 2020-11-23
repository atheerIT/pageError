from django.shortcuts import render
import socket


# Create your views here.

def index(request):
    print(request.META['REMOTE_ADDR'])
    print(socket.getfqdn(request.META['REMOTE_ADDR']))
    return render(request, 'localPage/index.html',{
        'comName':request.META['REMOTE_ADDR'],
        'ip':socket.getfqdn(request.META['REMOTE_ADDR'])
    })