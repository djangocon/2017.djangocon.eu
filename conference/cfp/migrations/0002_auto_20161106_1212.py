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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('author', models.CharField(max_length=400, verbose_name='Name')),
                ('email', models.EmailField(max_length=400, verbose_name='E-Mail')),
                ('author_bio', models.CharField(max_length=100, verbose_name='Bio')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('selected', models.BooleanField(default=False, verbose_name='Selected')),
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
            field=models.DateTimeField(auto_now_add=True, verbose_name='Submitted'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='mentor_offer',
            field=models.BooleanField(default=False, help_text='Are you an experienced speaker and are you willing to help other speakers? Select this and we will get in contact with you!', verbose_name='Mentor - Offer'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='mentor_wanted',
            field=models.BooleanField(default=False, help_text='More experienced speakers can help you reviewing your talk, practicing, and getting ready for the presentation', verbose_name='Mentor'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='pycon',
            field=models.BooleanField(default=False, help_text='We will share your proposal with the PyCon Italia Team and they will evaluate independently your proposal.', verbose_name='PyCon'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
