from random import randrange

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(req, name):
    return HttpResponse('<h1>Hello, world! id={0}</h1><button>ddd</button>'.format(name))


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def Manual(request, id):
    context = {}
    context['index'] = id
    return render(request, 'Manual.html', context)
