# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0003_auto_20161117_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='author_bio',
            field=models.CharField(max_length=400, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='proposal_why',
            field=models.TextField(verbose_name='Motivation', help_text='Explain here why your proposal is important for the attendees and what they will get from it.'),
        ),
        migrations.AlterField(
            model_name='workshopsubmission',
            name='author_bio',
            field=models.CharField(max_length=400, verbose_name='Bio'),
        ),
    ]
