# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.views.generic import DetailView, ListView

from conference.schedule.models import Slot


class SlotList(ListView):
    model = Slot
    context_object_name = 'talks'

    def get_context_data(self, **kwargs):
        context = super(SlotList, self).get_context_data(**kwargs)
        context['talks'] = super(SlotList, self).get_queryset().filter(sprint_days=False)
        context['workshops'] = super(SlotList, self).get_queryset().filter(sprint_days=True)
        return context


class SlotDetail(DetailView):
    model = Slot
    context_object_name = 'talk'

    def get_context_data(self, **kwargs):
        context = super(SlotDetail, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context
