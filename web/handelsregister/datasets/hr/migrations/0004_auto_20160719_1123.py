# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-19 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20160719_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handelsnaam',
            name='id',
        ),
        migrations.AddField(
            model_name='handelsnaam',
            name='handelsnaam',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='handelsnaam',
            name='macid',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=18, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maatschappelijkeactiviteit',
            name='nonMailing',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]