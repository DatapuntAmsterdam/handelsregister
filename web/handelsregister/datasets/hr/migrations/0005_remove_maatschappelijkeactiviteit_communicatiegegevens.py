# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-27 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_auto_20160719_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maatschappelijkeactiviteit',
            name='communicatiegegevens',
        ),
    ]
