# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_auto_20180111_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lakxya',
            name='awadhi',
            field=models.IntegerField(choices=[(3, '\u092c\u093e\u0930\u094d\u0937\u093f\u0915'), (0, '\u092a\u094d\u0930\u0925\u092e'), (1, '\u0926\u093f\u0924\u093f\u092f'), (2, '\u0924\u0943\u0924\u0940\u092f')], default=0, verbose_name='\u0905\u0935\u0927\u093f'),
        ),
        migrations.AlterField(
            model_name='pragati',
            name='awadhi',
            field=models.IntegerField(choices=[(3, '\u092c\u093e\u0930\u094d\u0937\u093f\u0915'), (0, '\u092a\u094d\u0930\u0925\u092e'), (1, '\u0926\u093f\u0924\u093f\u092f'), (2, '\u0924\u0943\u0924\u0940\u092f')], default=1, verbose_name='\u0905\u0935\u0927\u093f'),
        ),
    ]