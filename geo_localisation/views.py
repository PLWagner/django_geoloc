from django.http import HttpResponse
from django.shortcuts import render
from .models import MetaData
from .forms import SelectionBatimentForm


def accueil(request):
    data = MetaData.objects.all()
    return render(request, 'accueil.html')


def batiments(request):
    if request.method == 'GET':
        form = SelectionBatimentForm()
        data = MetaData.objects.all()
        return render(request, 'batiments.html', {'data': data, 'form': form})

    elif request.method == 'POST':
        form = SelectionBatimentForm(request.POST)
        if form.is_valid():
            batiment = form.cleaned_data['batiment']
            print("Le bâtient choisi est: " + batiment)


def details(request):
    if request.method == 'GET':
        data = MetaData.objects.filter(ID=22)
        return render(request, 'batiments.html', {'data': data})

