# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CFP(AppConfig):
    name = 'conference.cfp'
    verbose_name = _('CFP')


class CFPApp(CMSApp):
    name = 'CFP'
    _urls = ['conference.cfp.urls']
apphook_pool.register(CFPApp)


class WorkshopApp(CMSApp):
    name = 'Workshops'
    _urls = ['conference.cfp.workshop_urls']
apphook_pool.register(WorkshopApp)
