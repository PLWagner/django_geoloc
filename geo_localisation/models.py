#TODO COMMENTAIRES

from django.db import models


class MetaData(models.Model):
    ID = models.IntegerField(primary_key=True)
    MUNID = models.IntegerField(null=False)
    ARRID = models.CharField(max_length=5, null=False)
    CIV = models.CharField(max_length=5, null=False)
    GENERIQUE = models.CharField(max_length=15)
    SPECIFIQUE = models.CharField(max_length=30)
    COMPLET = models.CharField(max_length=45)
    COMPTE_FONCIER = models.CharField(max_length=8)
    NOM_PROPRIETAIRE = models.CharField(max_length=80)
    PRENOM_PROPRIETAIRE = models.CharField(max_length=80)
    COMPLET_ADR_PROP = models.CharField(max_length=100)
    VILLE_ADR_PROP = models.CharField(max_length=45)
    CP_ADR_PROP = models.CharField(max_length=6)
    VALEUR_BATIMENT = models.IntegerField()
    VALEUR_TERRAIN = models.IntegerField()
    REGL_USAGE = models.CharField(max_length=10)
    REGL_HAUTEUR = models.FloatField()
    REGL_ETAGES = models.CharField(max_length=8)
    REGL_DENSITE = models.CharField(max_length=8)
    REGL_IMPLANTATION = models.CharField(max_length=10)
    REGL_UNITE_PAYSAGE = models.CharField(max_length=50)
    ZONE_PATRIMOINE = models.CharField(max_length=100)
    TYPE_ZONE_PATRIMOINE = models.CharField(max_length=30)
    INTERET_IMMEUBLE = models.CharField(max_length=5)
    INTERET_QUARTIER = models.CharField(max_length=50)
    TAMPON_500_METRO = models.CharField(max_length=3)
    DESCRIPTION = models.CharField(max_length=254)
    LONGITUDE = models.FloatField()
    LATITUDE = models.FloatField()




