# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Schedule(AppConfig):
    name = 'conference.schedule'
    verbose_name = _('Schedule')


class ScheduleApp(CMSApp):
    name = 'Schedule'
    _urls = ['conference.schedule.urls']
apphook_pool.register(ScheduleApp)  # NOQA
