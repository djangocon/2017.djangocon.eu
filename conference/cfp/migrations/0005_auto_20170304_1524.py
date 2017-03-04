# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0004_auto_20161210_1721'),
    ]

    Submission = apps.get_model('cfp', 'Submission')
    WorkshopSubmission = apps.get_model('cfp', 'WorkshopSubmission')

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='proposal_audience',
            field=models.CharField(choices=Submission.AUDIENCE, verbose_name='Audience', max_length=10),
        ),
        migrations.AlterField(
            model_name='workshopsubmission',
            name='proposal_audience',
            field=models.CharField(choices=WorkshopSubmission.AUDIENCE, verbose_name='Audience', max_length=10),
        ),
        migrations.AlterField(
            model_name='workshopsubmission',
            name='workshop_duration',
            field=models.CharField(choices=WorkshopSubmission.DURATIONS, verbose_name='Duration', max_length=10),
        ),
    ]
