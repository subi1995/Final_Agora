# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-21 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20180518_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='rend_time',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='return_time',
            field=models.SmallIntegerField(default=0),
        ),
    ]
