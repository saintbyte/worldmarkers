import sys
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from rest_framework_gis.serializers import GeoModelSerializer, GeoFeatureModelSerializer, GeometrySerializerMethodField


class CountrySerializer(GeoModelSerializer):
    id = serializers.IntegerField(read_only=True, source='pk')

    class Meta:
        model = models.Country

        fields = (
            'id',
            'name',
            'area',
            'pop2005',
            'fips',
            'iso2',
            'iso3',
            'un',
            'region',
            'subregion',
            'center',
        )


class TownSerializer(GeoModelSerializer):
    id = serializers.IntegerField(read_only=True, source='pk')

    class Meta:
        model = models.Town
        fields = (
            'id',
            'geonameid',
            'name',
            'asciiname',
            'center',
            'is_capital',
            'feature_class',
            'feature_code',
            'country',
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
        )
