# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-16 08:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(default='EST', max_length=50)),
                ('bio', models.CharField(default='', max_length=1000)),
                ('member_type', models.CharField(choices=[('1', 'Senior Citizen'), ('2', 'Volunteer Driver'), ('3', 'Restaurant')], max_length=50)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
