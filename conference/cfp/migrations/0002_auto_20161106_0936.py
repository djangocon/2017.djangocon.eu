# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('author', models.CharField(max_length=400, verbose_name='Name')),
                ('email', models.EmailField(max_length=400, verbose_name='E-Mail')),
                ('author_bio', models.CharField(max_length=100, verbose_name='Bio')),
                ('created_at', models.DateTimeField(verbose_name='Submitted', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Updated', auto_now=True)),
                ('notes', models.TextField(verbose_name='Notes')),
                ('selected', models.BooleanField(verbose_name='Selected', default=False)),
                ('proposal_title', models.CharField(max_length=400, verbose_name='Title')),
                ('proposal_abstract', models.TextField(verbose_name='Abstract')),
                ('proposal_audience', models.CharField(max_length=10, verbose_name='Audience', choices=[('every', 'Everyone'), ('beginner', 'Beginner'), ('inter', 'Intermediate'), ('advanced', 'Advances')])),
                ('workshop_duration', models.CharField(max_length=10, verbose_name='Duration', choices=[('2hrs', 'Two Hours'), ('3hrs', 'Three Hours')])),
            ],
            options={
                'verbose_name': 'workshop submission',
                'verbose_name_plural': 'workshop submissions',
            },
        ),
        migrations.AlterField(
            model_name='submission',
            name='created_at',
            field=models.DateTimeField(verbose_name='Submitted', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='mentor_offer',
            field=models.BooleanField(help_text='Are you an experienced speaker and are you willing to help other speakers? Select this and we will get in contact with you!', verbose_name='Mentor - Offer', default=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='mentor_wanted',
            field=models.BooleanField(help_text='More experienced speakers can help you reviewing your talk, practicing, and getting ready for the presentation', verbose_name='Mentor', default=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='pycon',
            field=models.BooleanField(help_text='We will share your proposal with the PyCon Italia Team and they will evaluate independently your proposal.', verbose_name='PyCon', default=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='updated_at',
            field=models.DateTimeField(verbose_name='Updated', auto_now=True),
        ),
    ]
