# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.views.generic import ListView

from conference.schedule.models import Slot


class SlotView(ListView):
    model = Slot
