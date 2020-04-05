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


class Command(BaseCommand):
    help = _('Импортировать города')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        error_conntry_found_cnt = 0
        for town in Town.objects.all():
            try:
                c = Country.objects.get(iso2=town.country_code)
                town.country = c
                town.save()
            except:
                error_conntry_found_cnt = error_conntry_found_cnt + 1
        self.stdout.write(self.style.ERROR(
            'error_conntry_found_cnt:{}'.format(error_conntry_found_cnt)))
        self.stdout.write(self.style.SUCCESS('End'))
