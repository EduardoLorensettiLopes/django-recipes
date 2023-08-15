from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Eduardo Lorensetti',
    })


def sobre(request):
    return HttpResponse('Aqui é o sobre')


def contato(request):
    return HttpResponse('Aqui é o Contato')
