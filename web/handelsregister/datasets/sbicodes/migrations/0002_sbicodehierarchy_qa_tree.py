# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-20 12:49
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbicodes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbicodehierarchy',
            name='qa_tree',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
