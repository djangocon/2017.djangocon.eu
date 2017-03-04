# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import datetime
import os.path

from cms.models import Page
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from djmail.template_mail import MagicMailBuilder


def is_cfp_closed(closing_date):
    cfp_closing_date = datetime.datetime.strptime(closing_date, '%Y-%m-%d')
    return cfp_closing_date.date() <= datetime.date.today()


class SubmissionView(CreateView):
    thanks_page = 'thanks_cfp'
    closed_page = 'closed_cfp'
    closing_date = settings.CFP_CLOSING_DATE

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
            return Page.objects.public().get(reverse_id=self.thanks_page).get_absolute_url()
        except Page.DoesNotExist:
            return Page.objects.public().get_home().get_absolute_url()

    def get(self, request, *args, **kwargs):
        if is_cfp_closed(self.closing_date):
            redirect_url = Page.objects.public().get(reverse_id=self.closed_page).get_absolute_url()
            return HttpResponseRedirect(redirect_url)
        return super(SubmissionView, self).get(request, *args, **kwargs)
