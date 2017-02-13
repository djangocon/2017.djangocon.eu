# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.models import CMSPlugin
from django.core.management.base import NoArgsCommand

from conference.schedule.models import Slot


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        sections = [5001, 5020, 5011, 5003, 5007, 5018]
        plugins = CMSPlugin.objects.filter(parent__in=sections)
        levels = {
            5020: 'sponsors-row__platinum',
            5011: 'sponsors-row__gold',
            5003: 'sponsors-row__bronze',
            5007: 'sponsors-row__special',
            5018: 'sponsors-row__media',
        }
        for plugin in plugins:
            plugin, __ = plugin.get_plugin_instance()
            real_parent, __ = plugin.parent.get_plugin_instance()
            if real_parent.pk in levels:
                real_parent.app_data.layout.extra_classes = real_parent.app_data.layout.extra_classes.replace('rowsponsor-row', 'row sponsor-row')
                real_parent.app_data.layout.extra_classes = real_parent.app_data.layout.extra_classes.replace('sponsor-row', 'sponsors-row')
                print('fix', real_parent.app_data.layout.extra_classes)
                real_parent.save()
            if real_parent.pk in levels and levels[real_parent.pk] not in real_parent.app_data.layout.extra_classes:
                real_parent.app_data.layout.extra_classes += ' ' + levels[real_parent.pk]
                real_parent.save()
            if 'sponsors-row' in real_parent.app_data.layout.extra_classes and len(plugin.app_data.layout.extra_classes) == 0:
                plugin.app_data.layout.extra_classes = 'sponsor-level'
            plugin.app_data.layout.grid_width_s = None
            plugin.app_data.layout.grid_width_m = None
            plugin.app_data.layout.grid_width_l = None
            plugin.app_data.extended.grid_offset_s = None
            plugin.app_data.extended.grid_offset_m = None
            plugin.app_data.extended.grid_offset_l = None
            plugin.app_data.layout.grid_last_s = False
            plugin.app_data.layout.grid_last_m = False
            plugin.app_data.layout.grid_last_l = False
            plugin.save()
