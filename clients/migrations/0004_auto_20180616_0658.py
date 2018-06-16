# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-16 06:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0003_pickuprequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickuprequest',
            name='available_for',
        ),
        migrations.AddField(
            model_name='pickuprequest',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
