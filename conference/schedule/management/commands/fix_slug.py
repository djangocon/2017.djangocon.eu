# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.management.base import NoArgsCommand

from conference.schedule.models import Slot


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        for slot in Slot.objects.all():
            slot.save()
