# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url

from .views import SubmissionView
from .forms import WorkshopSubmissionForm
from .models import WorkshopSubmission

urlpatterns = [
    url(r'^', SubmissionView.as_view(form_class=WorkshopSubmissionForm,
                                     model=WorkshopSubmission),
                                     name='cfp_workshop_submission'),
]
