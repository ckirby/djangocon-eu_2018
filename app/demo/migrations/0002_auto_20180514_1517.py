# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='bathrooms',
            field=models.SmallIntegerField(verbose_name='Bathrooms'),
        ),
        migrations.AlterField(
            model_name='house',
            name='bedrooms',
            field=models.SmallIntegerField(verbose_name='Bedrooms'),
        ),
    ]
