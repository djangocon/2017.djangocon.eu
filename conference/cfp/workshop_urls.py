# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
from django.conf.urls import url

from .forms import WorkshopSubmissionForm
from .models import WorkshopSubmission
from .views import SubmissionView

urlpatterns = [
    url(r'^', SubmissionView.as_view(
        form_class=WorkshopSubmissionForm, model=WorkshopSubmission,
        thanks_page='thanks_workshop', closed_page='closed_workshop',
        closing_date=settings.WORKSHOP_CLOSING_DATE
    ), name='cfp_talks_submission'),
]
