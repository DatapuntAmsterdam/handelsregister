# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_dataselectie_rename'),
    ]

    operations = [
        migrations.AddField(
            model_name='locatie',
            name='huisletter',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='locatie',
            name='huisnummer',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='locatie',
            name='huisnummertoevoeging',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='locatie',
            name='postcode',
            field=models.CharField(blank=True, db_index=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='locatie',
            name='straatnaam',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locatie',
            name='toevoegingadres',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
