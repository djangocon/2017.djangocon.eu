# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os.path

from cms.models import Page
from django.conf import settings
from django.views.generic import CreateView
from djmail.template_mail import MagicMailBuilder

from .forms import SubmissionForm
from .models import Submission


class SubmissionView(CreateView):
    form_class = SubmissionForm
    model = Submission

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
        return Page.objects.public().get(reverse_id='thanks_cfp').get_absolute_url()
