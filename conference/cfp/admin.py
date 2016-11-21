# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ExportActionModelAdmin

from .models import Submission, WorkshopSubmission


def set_submission_as_selected(modeladmin, request, queryset):
    queryset.update(selected=True)
set_submission_as_selected.short_description = _("Set submission as 'Selected'")  # NOQA


@admin.register(Submission)
class TalkSubmissionAdmin(ExportActionModelAdmin):
    list_display = (
        'author', 'proposal_title', 'selected', 'pycon', 'created_at',
        'mentor_wanted', 'mentor_offer'
    )
    list_filter = ('selected', 'pycon')
    search_fields = ('author', 'proposal_title')
    actions = [set_submission_as_selected]


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
