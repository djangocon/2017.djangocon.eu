# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_slot_show_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='slides',
            field=models.URLField(null=True, verbose_name='Speaker slides', blank=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='video',
            field=models.URLField(null=True, verbose_name='Talk video', blank=True),
        ),
    ]
