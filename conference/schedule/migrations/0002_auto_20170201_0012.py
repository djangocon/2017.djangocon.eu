# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='mugshot',
            field=filer.fields.image.FilerImageField(blank=True, null=True, to='filer.Image', verbose_name='Speaker mughshot'),
        ),
        migrations.AddField(
            model_name='slot',
            name='schedule_abstract',
            field=models.TextField(blank=True, null=True, verbose_name='Schedule abstract'),
        ),
        migrations.AddField(
            model_name='slot',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=400, editable=False, verbose_name='Slug', blank=True, always_update=True, populate_from='generated_slug'),
        ),
        migrations.AddField(
            model_name='slot',
            name='twitter',
            field=models.CharField(default='', max_length=200, blank=True, verbose_name='Twitter'),
        ),
    ]
