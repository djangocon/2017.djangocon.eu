# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from conference.schedule.views import SlotView

urlpatterns = [
    url(r'^', SlotView.as_view(), name='talk_list')
]
