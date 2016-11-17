# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0002_auto_20161106_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(null=True, max_length=250, verbose_name='Name', help_text='Field for time slots that does not relate to a Talk or a Workshop.', blank=True)),
                ('day', models.DateField(verbose_name='Date')),
                ('start', models.TimeField(verbose_name='Start')),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('talk', models.ForeignKey(related_name='talks', null=True, to='cfp.Submission', blank=True)),
                ('workshop', models.ForeignKey(related_name='workshops', null=True, to='cfp.WorkshopSubmission', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Time slots',
                'verbose_name': 'Time slot',
                'ordering': ('day', 'start'),
            },
        ),
    ]
