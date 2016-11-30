from django.conf.urls import url
from geo_localisation.views import accueil, batiments, details, carte, bangarang

urlpatterns = [
    url(r'^$', accueil, name='accueil'),
    url(r'^batiments/$', batiments, name='batiments'),
    url(r'^bangarang/$', bangarang, name='bangarang'),
    url(r'^batiments/(\d+)/$', details, name='details'),
    url(r'^batiments/(\d+)/carte/$', carte, name='carte'),
]
