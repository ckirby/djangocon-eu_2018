# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20180514_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='square_meters',
            field=models.PositiveIntegerField(verbose_name='Sqaure Meters'),
        ),
    ]
