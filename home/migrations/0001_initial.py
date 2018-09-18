# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-12 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('actor', models.CharField(blank=True, max_length=255, null=True)),
                ('cata_log_name', models.CharField(blank=True, max_length=255, null=True)),
                ('cata_log_id', models.CharField(blank=True, max_length=255, null=True)),
                ('evaluation', models.FloatField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('is_use', models.IntegerField()),
                ('loc_name', models.CharField(blank=True, max_length=255, null=True)),
                ('loc_id', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('on_decade', models.CharField(blank=True, max_length=255, null=True)),
                ('plot', models.TextField(blank=True, null=True)),
                ('resolution', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_class_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_class_id', models.CharField(blank=True, max_length=255, null=True)),
                ('type_name', models.CharField(blank=True, max_length=255, null=True)),
                ('type_id', models.CharField(blank=True, max_length=255, null=True)),
                ('update_time', models.CharField(blank=True, max_length=255, null=True)),
                ('isvip', models.IntegerField(blank=True, db_column='isVip', null=True)),
            ],
            options={
                'db_table': 't_film',
            },
        ),
    ]
