# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-28 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sachibBaithak', '0015_auto_20180128_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetbaktabya',
            name='karyakram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.KaryaKram', verbose_name='\u0915\u093e\u0930\u094d\u092f\u0915\u094d\u0930\u092e\u0939\u0930\u0941 '),
        ),
    ]
