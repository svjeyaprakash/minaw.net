# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynimg', '0008_auto_20160829_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageurl',
            name='dwnlTime',
            field=models.DurationField(blank=True, null=True, verbose_name='Average download time'),
        ),
    ]