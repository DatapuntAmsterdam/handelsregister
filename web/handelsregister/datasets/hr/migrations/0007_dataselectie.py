# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-31 10:27
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_geovbo_bag_numid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetrokkenPersonen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_naam', models.CharField(help_text='Maatschappelijke activiteit naam', max_length=600)),
                ('kvk_nummer', models.CharField(blank=True, help_text='Kvk nummer', max_length=8, null=True)),
                ('persoons_id', models.IntegerField(null=True)),
                ('rol', models.CharField(blank=True, help_text='Rol', max_length=14, null=True)),
                ('naam', models.CharField(blank=True, help_text='Persoonsnaam (handelsregister terminologie)', max_length=600, null=True)),
                ('rechtsvorm', models.CharField(blank=True, help_text='Rechtsvorm', max_length=50, null=True)),
                ('functietitel', models.CharField(blank=True, help_text='Titel van de functionaris', max_length=20, null=True)),
                ('soortbevoegdheid', models.CharField(blank=True, help_text='Bevoegdheid van de functionaris', max_length=20, null=True)),
                ('bevoegde_naam', models.CharField(blank=True, help_text='Bevoegdheid van de functionaris', max_length=240, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'hr_betrokken_personen',
            },
        ),

        migrations.CreateModel(
            name='CBS_sbi_hoofdcat',
            fields=[
                ('hcat', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('hoofdcategorie', models.CharField(max_length=140)),
            ],
        ),

        migrations.CreateModel(
            name='CBS_sbi_subcat',
            fields=[
                ('scat', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subcategorie', models.CharField(max_length=140)),
                ('hcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CBS_sbi_hoofdcat')),
            ],
        ),
        migrations.CreateModel(
            name='CBS_sbicodes',
            fields=[
                ('sbi_code', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('sub_sub_categorie', models.CharField(max_length=140)),
                ('scat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.CBS_sbi_subcat')),
            ],
        ),
        migrations.CreateModel(
            name='DataSelectie',
            fields=[
                ('vestiging_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('api_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
