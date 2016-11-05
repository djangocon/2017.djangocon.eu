# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from .views import SubmissionView

from .forms import TalkSubmissionForm
from .models import TalkSubmission

urlpatterns = [
    url(r'^', SubmissionView.as_view(form_class=TalkSubmissionForm,
                                     model=TalkSubmission),
                                     name='cfp_talks_submission'),
]
