from django.http import HttpResponse
from django.shortcuts import render
from .models import MetaData
import googlemaps


# Create your views here.

def index(request):
    data = MetaData.objects.all()
    # return HttpResponse("Allo        " + str(data))

    return render(request, 'batiments.html', {'data': data})
