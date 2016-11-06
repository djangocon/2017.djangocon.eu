# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from .forms import TalkSubmissionForm
from .models import Submission
from .views import SubmissionView

urlpatterns = [
    url(r'^', SubmissionView.as_view(
        form_class=TalkSubmissionForm, model=Submission
    ), name='cfp_talks_submission'),
]
