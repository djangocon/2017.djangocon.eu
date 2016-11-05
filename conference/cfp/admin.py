# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin

from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(ExportActionModelAdmin):
    list_display = (
        'author', 'proposal_title', 'selected', 'pycon', 'created_at', 'mentor_wanted',
        'mentor_offer'
    )
    list_filter = ('selected', 'pycon')
    search_fields = ('author', 'proposal_title')


class SubmissionData(resources.ModelResource):
    class Meta:
        model = Submission
