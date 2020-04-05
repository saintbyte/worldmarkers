__author__ = 'sb'
import os
import sys
import datetime
import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.contrib.gis.utils import LayerMapping
from world.models import Country, Town
from django.utils.translation import gettext_lazy as _


class geonames_csv_dialect(csv.Dialect):
    """Describe the usual properties of Geonames.org-generated CSV files."""
    delimiter = '\t'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL


csv.register_dialect("geonames_csv_dialect", geonames_csv_dialect)


class Command(BaseCommand):
    help = _('Импортировать города')
    fiedls_names = [
        'geonameid',
        'name',
        'asciiname',
        'alternatenames',
        'latitude',
        'longitude',
        'feature_class',
        'feature_code',
        'country_code',
        'cc2',
        'admin1_code',
        'admin2_code',
        'admin3_code',
        'admin4_code',
        'population',
        'elevation',
        'dem',
        'timezone',
        'modification_date',
    ]

    def add_arguments(self, parser):
        parser.add_argument('--file', nargs='?', type=str, help=_(
            "Файл для загрузки в базу  ( например  путь к cities15000.txt )  "))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        if not options['file']:
            self.stdout.write(self.style.ERROR(_('Укажите файл для импорта')))
            quit()
        fh = open(options['file'], newline='', encoding='utf-8')
        reader = csv.DictReader(fh,
                                fieldnames=self.fiedls_names,
                                dialect=geonames_csv_dialect)
        for row in reader:
            row2 = row.copy()
            row2['center'] = Point(
                float(row2['longitude']), float(row2['latitude']))
            row2['modification_date'] = datetime.datetime.strptime(
                row2['modification_date'], '%Y-%m-%d')
            del(row2['longitude'])
            del(row2['latitude'])
            if row2['elevation'] == '':
                row2['elevation'] = 0
            t = Town(**row2)
            t.save()
        fh.close()
        self.stdout.write(self.style.SUCCESS('End'))
