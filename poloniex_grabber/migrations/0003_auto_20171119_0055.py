# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poloniex_grabber', '0002_auto_20171118_2359'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PoloniexCoinPairDataCandles',
        ),
        migrations.AddField(
            model_name='poloniexcoinpairdataraw',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
