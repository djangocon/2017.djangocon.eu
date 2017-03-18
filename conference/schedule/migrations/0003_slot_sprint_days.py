# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20170201_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='sprint_days',
            field=models.BooleanField(verbose_name='Part of sprint days', default=False),
        ),
    ]
