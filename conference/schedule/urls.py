# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from conference.schedule.views import SlotDetail, SlotList

urlpatterns = [
    url(r'^(?P<slug>[\w.@+-]+)/$', SlotDetail.as_view(), name='talk-detail'),
    url(r'^', SlotList.as_view(), name='talk-list'),
]
