from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название'))
    area = models.IntegerField(default=0, verbose_name=_('Площадь'))
    pop2005 = models.IntegerField(verbose_name=_('Популяция на 2005'))
    fips = models.CharField(verbose_name=_('FIPS Код'),
                            max_length=2, default=0, null=True)
    iso2 = models.CharField(verbose_name=_('2 Цифровой код ISO'), max_length=2)
    iso3 = models.CharField(verbose_name=_(
        '3 Цифровой код  ISO'), max_length=3)
    un = models.IntegerField(verbose_name=_('Код ООН'))
    region = models.IntegerField(verbose_name=_('Код региона'))
    subregion = models.IntegerField(verbose_name=_('Суб региона код '))
    center = models.PointField(verbose_name=_('Центр'), geography=True, dim=2)
    mpoly = models.MultiPolygonField(verbose_name=_('Полигон всей страны'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Страна')
        verbose_name_plural = _('Страны')


class Town(models.Model):
    geonameid = models.IntegerField(default=0,
                                    verbose_name=_('Geonameid'),
                                    help_text=_('Id в базе geonames'))
    name = models.CharField(max_length=200,
                            verbose_name=_('Название'),
                            default='',
                            help_text=_('Название точки на карте'))
    description = models.TextField(max_length=20000,
                                   verbose_name=_('Описание'),
                                   default='',
                                   help_text=_('Описание'))
    asciiname = models.CharField(max_length=200,
                                 verbose_name=_('Ascii название'),
                                 default='',
                                 help_text=_('Название географической точки  в простых ascii символах'))
    alternatenames = models.CharField(max_length=10000,
                                      verbose_name=_('Алтернативные названия'),
                                      default='',
                                      help_text=_('Алтернативные названия, разделенные запятой, ascii names automatically transliterated, convenience attribute from alternatename table'))
    center = models.PointField(verbose_name=_('Центр'),
                               geography=True,
                               dim=2)
    is_capital = models.BooleanField(
        default=False, verbose_name=_('Capital of country'))
    feature_class = models.CharField(max_length=1,
                                     verbose_name=_('Feature class'),
                                     default='',
                                     help_text=_('see http://www.geonames.org/export/codes.html'))
    feature_code = models.CharField(max_length=10,
                                    verbose_name=_('Feature code'),
                                    default='',
                                    help_text=_('see http://www.geonames.org/export/codes.html'))
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                verbose_name=_('Страна'))
    country_code = models.CharField(max_length=2,
                                    verbose_name=_('Код страны'),
                                    default='',
                                    help_text=_('ISO-3166 2-буквенный код страны'))
    cc2 = models.CharField(max_length=200,
                           verbose_name=_('Alternate country codes'),
                           default='',
                           help_text=_('Alternate country codes, comma separated, ISO-3166 2-letter country code'))
    admin1_code = models.CharField(max_length=20,
                                   verbose_name=_('Fips code'),
                                   default='',
                                   help_text=_('fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code'))
    admin2_code = models.CharField(max_length=80,
                                   verbose_name=_(
                                       'Code for the second administrative division'),
                                   default='',
                                   help_text=_('code for the second administrative division, a county in the US, see file admin2Codes.txt'))
    admin3_code = models.CharField(max_length=20,
                                   verbose_name=_('admin3 code'),
                                   default='',
                                   help_text=_('code for third level administrative division'))
    admin4_code = models.CharField(max_length=20,
                                   verbose_name=_('admin4 code'),
                                   default='',
                                   help_text=_('code for fourth level administrative division'))
    population = models.IntegerField(default=0, verbose_name=_('Население'))
    elevation = models.IntegerField(default=0, verbose_name=_(
        'Высота'), help_text=_('elevation in meters'))
    dem = models.IntegerField(default=0,
                              verbose_name=_('Digital Elevation model'),
                              help_text=_('digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.'))
    timezone = models.CharField(max_length=40,
                                verbose_name=_('Часовой пояс'),
                                default='',
                                help_text=_('the iana timezone id(see file timeZone.txt)'))
    modification_date = models.DateField(default=now,
                                         verbose_name=_('Дата изменения'),
                                         help_text=_('date of last modification in yyyy-MM-dd format'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')


class TownImages(models.Model):
    town = models.ForeignKey(Town,
                             on_delete=models.CASCADE,
                             verbose_name=_('Город'))
    image = models.ImageField(upload_to='photos',  verbose_name=_('Фотография'))

    class Meta:
        verbose_name = _('Фотография')
        verbose_name_plural = _('Фотографии')
