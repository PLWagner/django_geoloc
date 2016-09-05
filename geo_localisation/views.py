from django.shortcuts import render
from .models import MetaData


def accueil(request):
    return render(request, 'accueil.html')


def batiments(request):
    if request.method == 'GET':
        data = MetaData.objects.all()
        return render(request, 'batiments.html', {'data': data})


def details(request, num):
    if request.method == 'GET':
        batiments = True
        data = MetaData.objects.filter(ID=num)[0]
        return render(request, 'details.html', {'data': data, 'batiments': batiments})


def carte(request, num):
    if request.method == 'GET':
        details = True
        data = MetaData.objects.filter(ID=num)[0]
        return render(request, 'carte.html', {'data': data, 'details': details})
