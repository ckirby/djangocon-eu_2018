# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Bedrooms')),
                ('bathrooms', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], verbose_name='Bathrooms')),
                ('heat', models.CharField(choices=[('NG', 'Natural Gas'), ('Elec', 'Electric'), ('Wood', 'Wood')], max_length=4, verbose_name='Heating')),
                ('square_meters', models.IntegerField(verbose_name='Sqaure Meters')),
                ('has_garage', models.BooleanField(verbose_name='Garage?')),
            ],
        ),
    ]
