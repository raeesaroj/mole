# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-20 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0050_merge_20180620_0632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlykaryakram',
            old_name='monthlykaryakram',
            new_name='monthly_karyakram',
        ),
        migrations.RemoveField(
            model_name='pragati',
            name='office',
        ),
        migrations.AlterField(
            model_name='lakxya',
            name='datesubmited',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lakxya',
            name='dateupdated',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monthlykaryakram',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_karyakram', to='office.Office', verbose_name='\u0915\u093e\u0930\u094d\u092f\u093e\u0932\u092f'),
        ),
        migrations.AlterField(
            model_name='monthlyprogress',
            name='datesubmited',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyprogress',
            name='dateupdated',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyprogress',
            name='pragati',
            field=models.TextField(default=1, verbose_name='\u092e\u0939\u093f\u0928\u093e\u0915\u094b \u092a\u094d\u0930\u0917\u0924\u0940'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pragati',
            name='datesubmited',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pragati',
            name='dateupdated',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]