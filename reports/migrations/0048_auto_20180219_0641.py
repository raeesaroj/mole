# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-19 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0047_merge_20180201_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyprogress',
            name='pragati',
        ),
        migrations.AddField(
            model_name='monthlyprogress',
            name='progress',
            field=models.TextField(blank=True, null=True, verbose_name='\u092e\u0939\u093f\u0928\u093e\u0915\u094b \u092a\u094d\u0930\u0917\u0924\u0940'),
        ),
    ]
