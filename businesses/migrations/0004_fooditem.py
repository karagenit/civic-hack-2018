# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-16 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0003_auto_20180616_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('number', models.IntegerField(default=0)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='businesses.Business')),
            ],
        ),
    ]