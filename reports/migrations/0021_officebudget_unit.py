# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-17 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0020_auto_20180116_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='officebudget',
            name='unit',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='\u092f\u0941\u0928\u093f\u091f'),
        ),
    ]
