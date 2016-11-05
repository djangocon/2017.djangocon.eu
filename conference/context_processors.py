# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings


def context_settings(request):
    context = dict()
    context['GOOGLE_ANALYTICS_ID'] = settings.GOOGLE_ANALYTICS_ID
    return context
