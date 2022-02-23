

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'v2/index.html')


def name(request):
    return render(request, 'v2/name.html', {'name':'Joy'})


def username(request, keyword):
    return render(request, 'v2/name.html', {'name':keyword})