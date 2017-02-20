# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin

from .models import Slot


class SlotResource(resources.ModelResource):

    class Meta:
        model = Slot
        fields = (
            'talk__proposal_title', 'day', 'start', 'duration', 'talk__author', 'talk__author_bio',
            'talk__proposal_abstract', 'talk__proposal_audience', 'twitter', 'mugshot'
        )


@admin.register(Slot)
class SlotAdmin(ExportActionModelAdmin):
    list_display = ('title', 'day', 'start', 'parsed_duration', 'is_talk', 'is_workshop', 'is_custom')
    search_fields = ('talk__author', 'talk__proposal_title', 'workshop__author', 'workshop__proposal_title')
    resource_class = SlotResource
    readonly_fields = ('slug',)
