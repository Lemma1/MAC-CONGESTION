# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-14 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='philly_link',
            name='zoom_level',
            field=models.IntegerField(default=0),
        ),
    ]