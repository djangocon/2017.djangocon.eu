# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_slot_sprint_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='show_end_time',
            field=models.BooleanField(verbose_name='Show end time in schedule', default=False),
        ),
    ]
