# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-11 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vestiging',
            name='vestigingsnummer',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
