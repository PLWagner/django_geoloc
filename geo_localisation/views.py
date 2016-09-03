from django.http import HttpResponse
from django.shortcuts import render
from .models import MetaData


# Create your views here.

def index(request):
    data = MetaData.objects.filter(ID=23)[0]
    return HttpResponse("Allo        " + str(data.ARRID))
