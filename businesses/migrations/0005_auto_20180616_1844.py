# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-16 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0004_fooditemclass_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditemclass',
            name='calories',
            field=models.IntegerField(null=True),
        ),
    ]
