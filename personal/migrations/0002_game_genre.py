# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(default='Action', max_length=140),
            preserve_default=False,
        ),
    ]
