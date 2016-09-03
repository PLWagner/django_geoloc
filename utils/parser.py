# -*- coding: utf-8 -*-
# TODO COMMENTAIRES
import codecs
import csv
from geo_localisation.models import MetaData


class Parser:
    @staticmethod
    def insert_data():

        with codecs.open('data/sause01direction01directiondonneesouvertesbatimentsvacantsbatimentsvacantsvm2015.csv',
                         'r', encoding='utf-8', errors='replace') as data:
            fields = ('ID',
                      'MUNID',
                      'ARRID',
                      'CIV',
                      'GENERIQUE',
                      'SPECIFIQUE',
                      'COMPLET',
                      'COMPTE_FONCIER',
                      'NOM_PROPRIETAIRE',
                      'PRENOM_PROPRIETAIRE',
                      'COMPLET_ADR_PROP',
                      'VILLE_ADR_PROP',
                      'CP_ADR_PROP',
                      'VALEUR_BATIMENT',
                      'VALEUR_TERRAIN',
                      'REGL_USAGE',
                      'REGL_HAUTEUR',
                      'REGL_ETAGES',
                      'REGL_DENSITE',
                      'REGL_IMPLANTATION',
                      'REGL_UNITE_PAYSAGE',
                      'ZONE_PATRIMOINE',
                      'TYPE_ZONE_PATRIMOINE',
                      'INTERET_IMMEUBLE',
                      'INTERET_QUARTIER',
                      'TAMPON_500_METRO',
                      'DESCRIPTION',
                      'LONGITUDE',
                      'LATITUDE')

            reader = csv.DictReader(data, fieldnames=fields)
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                else:
                    metadata = MetaData.objects.create(ID=row.get('ID'),
                                                       MUNID=row.get('MUNID'),
                                                       ARRID=row.get('ARRID'),
                                                       CIV=row.get('CIV'),
                                                       GENERIQUE=row.get('GENERIQUE'),
                                                       SPECIFIQUE=row.get('SPECIFIQUE'),
                                                       COMPLET=row.get('COMPLET'),
                                                       COMPTE_FONCIER=row.get('COMPTE_FONCIER'),
                                                       NOM_PROPRIETAIRE=row.get('NOM_PROPRIETAIRE'),
                                                       PRENOM_PROPRIETAIRE=row.get('PRENOM_PROPRIETAIRE'),
                                                       COMPLET_ADR_PROP=row.get('COMPLET_ADR_PROP'),
                                                       VILLE_ADR_PROP=row.get('VILLE_ADR_PROP'),
                                                       CP_ADR_PROP=row.get('CP_ADR_PROP'),
                                                       REGL_USAGE=row.get('REGL_USAGE'),
                                                       VALEUR_BATIMENT=row.get('VALEUR_BATIMENT'),
                                                       VALEUR_TERRAIN=row.get('VALEUR_TERRAIN'),
                                                       REGL_HAUTEUR=row.get('REGL_HAUTEUR'),
                                                       REGL_ETAGES=row.get('REGL_ETAGES'),
                                                       REGL_DENSITE=row.get('REGL_DENSITE'),
                                                       REGL_IMPLANTATION=row.get('REGL_IMPLANTATION'),
                                                       REGL_UNITE_PAYSAGE=row.get('REGL_UNITE_PAYSAGE'),
                                                       ZONE_PATRIMOINE=row.get('ZONE_PATRIMOINE'),
                                                       TYPE_ZONE_PATRIMOINE=row.get('TYPE_ZONE_PATRIMOINE'),
                                                       INTERET_IMMEUBLE=row.get('INTERET_IMMEUBLE'),
                                                       INTERET_QUARTIER=row.get('INTERET_QUARTIER'),
                                                       TAMPON_500_METRO=row.get('TAMPON_500_METRO'),
                                                       DESCRIPTION=row.get('DESCRIPTION'),
                                                       LONGITUDE=row.get('LONGITUDE'),
                                                       LATITUDE=row.get('LATITUDE'),
                                                       )
                    metadata.save()
                    count += 1
