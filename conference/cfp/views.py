# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import datetime
import os.path

from cms.models import Page
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from djmail.template_mail import MagicMailBuilder


def is_cfp_closed():
    cfp_closing_date = datetime.datetime.strptime(settings.CFP_CLOSING_DATE, '%Y-%m-%d')
    return cfp_closing_date.date() <= datetime.date.today()


class SubmissionView(CreateView):
    def _send_notification(self):
        if self.object:
            with open(os.path.join(settings.STATIC_ROOT, 'css', 'style.css'), 'r') as css_file:
                css = css_file.read()
            context = {
                'css': css,
                'instance': self.object
            }
            email = MagicMailBuilder()
            notification = email.submission_notification(self.object.email, context)
            notification.send()

    def get_success_url(self):
        self._send_notification()
        try:
            return Page.objects.public().get(reverse_id='thanks_cfp').get_absolute_url()
        except Page.DoesNotExist:
            return Page.objects.public().get_home()

    def get(self, request, *args, **kwargs):
        # TODO redirect to different template in case of closing
        if is_cfp_closed():
            redirect_url = Page.objects.public().get(reverse_id='closed_cfp').get_absolute_url()
            return HttpResponseRedirect(redirect_url)
        return super(SubmissionView, self).get(request, *args, **kwargs)
