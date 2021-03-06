# Generated by Django 3.0.4 on 2020-04-01 16:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name='Популяция на 2005')),
                ('fips', models.CharField(max_length=2, verbose_name='FIPS Код')),
                ('iso2', models.CharField(max_length=2, verbose_name='2 D ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(verbose_name='United Nations Code')),
                ('region', models.IntegerField(verbose_name='Region Code')),
                ('subregion', models.IntegerField(verbose_name='Sub-Region Code')),
                ('center', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='center')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name': 'Страны',
            },
        ),
    ]
