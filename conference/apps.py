# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Conference(AppConfig):
    name = 'conference'
    verbose_name = _('Conference')
