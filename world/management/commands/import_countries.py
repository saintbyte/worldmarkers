__author__ = 'sb'
import os
import sys
import math
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.contrib.gis.utils import LayerMapping
from world.models import Country
from django.utils.translation import gettext_lazy as _


class MyLayerMapping(LayerMapping):

    def calculate_custom_kwargs(self, feat):
        return {'center': Point(feat['lon'].value, feat['lat'].value)}

    def check_layer(self):
        super().check_layer()
        self.fields['center'] = self.model.center

    def feature_kwargs(self, feat):
        kwargs = super().feature_kwargs(feat)
        kwargs.update(self.calculate_custom_kwargs(feat))
        return kwargs


class Command(BaseCommand):
    help = _('Импортировать страны')

    def add_arguments(self, parser):
        parser.add_argument('--file', nargs='?', type=str, help=_(
            "Shp для загрузки в базу  ( путь к TM_WORLD_BORDERS-0.3.shp )  "))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        world_mapping = {
            'fips': 'FIPS',
            'iso2': 'ISO2',
            'iso3': 'ISO3',
            'un': 'UN',
            'name': 'NAME',
            'area': 'AREA',
            'pop2005': 'POP2005',
            'region': 'REGION',
            'subregion': 'SUBREGION',
            'mpoly': 'MULTIPOLYGON',
        }
        if not options['file']:
            self.stdout.write(self.style.ERROR(_('Укажите файл для импорта')))
            quit()
        world_shp = options['file']
        Country.objects.all().delete()
        lm = MyLayerMapping(Country,
                            world_shp,
                            world_mapping,
                            transform=False)
        lm.save(strict=True, verbose=True)
        self.stdout.write(self.style.SUCCESS('End'))
