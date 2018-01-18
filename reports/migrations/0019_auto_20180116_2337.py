# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-16 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0018_remove_karyakram_fiscal_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='lakxya',
            name='fiscal_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.FiscalYear', verbose_name='\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u0935\u0930\u094d\u0937'),
        ),
        migrations.AddField(
            model_name='pragati',
            name='fiscal_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.FiscalYear', verbose_name='\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u0935\u0930\u094d\u0937'),
        ),
    ]
