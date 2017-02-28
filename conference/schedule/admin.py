# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from import_export.admin import ExportMixin

from .models import Slot


@admin.register(Slot)
class SlotAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'day', 'start', 'parsed_duration', 'is_talk', 'is_workshop', 'is_custom')
    search_fields = ('talk__author', 'talk__proposal_title', 'workshop__author', 'workshop__proposal_title')

    readonly_fields = ('slug',)
    date_hierarchy = 'day'
