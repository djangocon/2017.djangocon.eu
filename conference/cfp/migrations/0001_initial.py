# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=400, verbose_name='Name')),
                ('email', models.EmailField(max_length=400, verbose_name='E-Mail')),
                ('author_bio', models.CharField(max_length=100, verbose_name='Bio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('proposal_title', models.CharField(max_length=400, verbose_name='Title')),
                ('proposal_abstract', models.TextField(verbose_name='Abstract')),
                ('proposal_why', models.TextField(verbose_name='Motivation')),
                ('proposal_requirements', models.TextField(default='', verbose_name='Requirements')),
                ('proposal_audience', models.CharField(max_length=10, verbose_name='Audience', choices=[('every', 'Everyone'), ('beginner', 'Beginner'), ('inter', 'Intermediate'), ('advanced', 'Advances')])),
                ('mentor_wanted', models.BooleanField(default=False, verbose_name='Mentor')),
                ('mentor_offer', models.BooleanField(default=False, verbose_name='Mentor - Offer')),
                ('notes', models.TextField(verbose_name='Notes')),
                ('pycon', models.BooleanField(default=False, verbose_name='PyCon')),
                ('selected', models.BooleanField(default=False, verbose_name='Selected')),
            ],
            options={
                'verbose_name': 'talk submission',
                'verbose_name_plural': 'talk submissions',
            },
        ),
    ]
