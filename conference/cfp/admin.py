# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin

from .models import Submission, WorkshopSubmission


@admin.register(Submission)
class TalkSubmissionAdmin(ExportActionModelAdmin):
    list_display = (
        'author', 'proposal_title', 'selected', 'pycon', 'created_at',
        'mentor_wanted', 'mentor_offer'
    )
    list_filter = ('selected', 'pycon')
    search_fields = ('author', 'proposal_title')


class TalkSubmissionData(resources.ModelResource):
    class Meta:
        model = Submission


@admin.register(WorkshopSubmission)
class WorkshopSubmissionAdmin(ExportActionModelAdmin):
    list_display = (
        'author', 'proposal_title', 'selected', 'workshop_duration', 'created_at'
    )
    list_filter = ('selected', 'proposal_audience')
    search_fields = ('author', 'proposal_title')


class WorkshopSubmissionData(resources.ModelResource):
    class Meta:
        model = WorkshopSubmission
