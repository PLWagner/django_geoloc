from django.conf.urls import include, url
from django.contrib import admin
from geo_localisation.views import accueil, batiments, details

urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^batiments', batiments, name='batiments'),
    url(r'^batiments/?$/details', details, name='details'),
]
