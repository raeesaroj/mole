# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20170713_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
