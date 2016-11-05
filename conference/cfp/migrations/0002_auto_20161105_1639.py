# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalkSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('author', models.CharField(verbose_name='Name', max_length=400)),
                ('email', models.EmailField(verbose_name='E-Mail', max_length=400)),
                ('author_bio', models.CharField(verbose_name='Bio', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted')),
                ('updated_at', models.DateTimeField(verbose_name='Updated', auto_now=True)),
                ('notes', models.TextField(verbose_name='Notes')),
                ('selected', models.BooleanField(default=False, verbose_name='Selected')),
                ('proposal_title', models.CharField(verbose_name='Title', max_length=400)),
                ('proposal_abstract', models.TextField(verbose_name='Abstract')),
                ('proposal_audience', models.CharField(choices=[('every', 'Everyone'), ('beginner', 'Beginner'), ('inter', 'Intermediate'), ('advanced', 'Advances')], verbose_name='Audience', max_length=10)),
                ('proposal_why', models.TextField(verbose_name='Motivation')),
                ('proposal_requirements', models.TextField(default='', verbose_name='Requirements')),
                ('mentor_wanted', models.BooleanField(default=False, verbose_name='Mentor', help_text='More experienced speakers can help you reviewing your talk, practicing, and getting ready for the presentation')),
                ('mentor_offer', models.BooleanField(default=False, verbose_name='Mentor - Offer', help_text='Are you an experienced speaker and are you willing to help other speakers? Select this and we will get in contact with you!')),
                ('pycon', models.BooleanField(default=False, verbose_name='PyCon', help_text='We will share your proposal with the PyCon Italia Team and they will evaluate independently your proposal.')),
            ],
            options={
                'verbose_name': 'talk submission',
                'verbose_name_plural': 'talk submissions',
            },
        ),
        migrations.CreateModel(
            name='WorkshopSubmission',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('author', models.CharField(verbose_name='Name', max_length=400)),
                ('email', models.EmailField(verbose_name='E-Mail', max_length=400)),
                ('author_bio', models.CharField(verbose_name='Bio', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted')),
                ('updated_at', models.DateTimeField(verbose_name='Updated', auto_now=True)),
                ('notes', models.TextField(verbose_name='Notes')),
                ('selected', models.BooleanField(default=False, verbose_name='Selected')),
                ('proposal_title', models.CharField(verbose_name='Title', max_length=400)),
                ('proposal_abstract', models.TextField(verbose_name='Abstract')),
                ('proposal_audience', models.CharField(choices=[('every', 'Everyone'), ('beginner', 'Beginner'), ('inter', 'Intermediate'), ('advanced', 'Advances')], verbose_name='Audience', max_length=10)),
                ('workshop_duration', models.CharField(choices=[('2_hrs', 'Two Hours'), ('3_hrs', 'Three Hours')], verbose_name='Durtation', max_length=10)),
            ],
            options={
                'verbose_name': 'workshop submission',
                'verbose_name_plural': 'workshop submissions',
            },
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]
