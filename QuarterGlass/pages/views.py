from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
from deneme import DenemeThread

sonuc = DenemeThread()
sonuc.start()


def index(request):
    dest1 = Destination()
    dest1.bodyNo = 12344

    i = sonuc.result()
    dest1.assyNo = i
    dest1.spek = 'Corolla Siyah'
    dest1.result = 'NG'

    return render(request, 'pages/index.html', {'dest1': dest1})


def about(request):
    return render(request, 'pages/about.html')
