from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Country, Town, TownImages
from django.utils.translation import gettext_lazy as _

class CountryAdmin(LeafletGeoAdmin):
    search_fields = [
        'name',
        'fips',
        'iso2',
        'iso3',
        'un',
    ]


admin.site.register(Country, CountryAdmin)


class TownImagesInline(admin.TabularInline):
    model = TownImages
    extra = 1

    class Meta:
        verbose_name = _('Связь города с фотографией')
        verbose_name_plural = _('Связь города с фотографией')


class TownAdmin(LeafletGeoAdmin):
    search_fields = [
        'name',
        'description',
        'asciiname',
        'alternatenames',
        'feature_class',
        'feature_code',
        'country_code',
        'cc2',
        'admin1_code',
        'admin2_code',
        'admin3_code',
        'admin4_code',
        
    ]
    autocomplete_fields = ['country',]
    inlines = [TownImagesInline, ]


admin.site.register(Town, TownAdmin)
