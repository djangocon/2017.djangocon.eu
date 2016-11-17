# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0002_auto_20161106_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='notes',
            field=models.TextField(verbose_name='Notes', help_text='Write here if you have any further notes regarding your proposal.', blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='proposal_abstract',
            field=models.TextField(verbose_name='Abstract', help_text='This text will be published on the website if the talk is accepted.'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='proposal_why',
            field=models.TextField(verbose_name='Motivation', help_text='Explain here why your proposal is important for the attendees an what they will get from it.'),
        ),
        migrations.AlterField(
            model_name='workshopsubmission',
            name='notes',
            field=models.TextField(verbose_name='Notes', help_text='Write here if you have any further notes regarding your proposal.', blank=True),
        ),
        migrations.AlterField(
            model_name='workshopsubmission',
            name='proposal_abstract',
            field=models.TextField(verbose_name='Abstract', help_text='This text will be published on the website if the talk is accepted.'),
        ),
    ]
