# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_game_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='tag',
            field=models.ManyToManyField(to='personal.Tag'),
        ),
    ]