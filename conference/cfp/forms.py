# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

from conference.cfp.models import Submission, WorkshopSubmission


class TalkSubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = (
            'author', 'email', 'author_bio', 'proposal_title',
            'proposal_abstract', 'proposal_why', 'proposal_requirements', 'proposal_audience',
            'mentor_wanted', 'mentor_offer', 'notes', 'pycon'
        )

    def __init__(self, *args, **kwargs):
        super(TalkSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = _('Your name')
        self.fields['email'].label = _('Your email')
        self.fields['author_bio'].label = _('Tell us about yourself')
        self.fields['proposal_title'].label = _('Your proposal\'s title')
        self.fields['proposal_abstract'].label = _('Abstract of your proposal')
        self.fields['proposal_why'].label = _('What the audience will get from your proposal?')
        self.fields['proposal_requirements'].label = _(
            'Do you have any special requirement for your talk?'
        )
        self.fields['proposal_audience'].label = _(
            'What\'s the intended audience of your proposal?')
        self.fields['mentor_wanted'].label = _('I\'d like a mentor')
        self.fields['mentor_offer'].label = _('I\'m volunteering as mentor')
        self.fields['pycon'].label = _('Do you want to submit your proposal to PyCon Italia 2017?')


class WorkshopSubmissionForm(forms.ModelForm):

    class Meta:
        model = WorkshopSubmission
        fields = (
            'author', 'email', 'author_bio', 'proposal_title',
            'proposal_abstract', 'proposal_audience', 'workshop_duration',
            'notes'
        )

    def __init__(self, *args, **kwargs):
        super(WorkshopSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = _('Your name')
        self.fields['email'].label = _('Your email')
        self.fields['author_bio'].label = _('Tell us about yourself')
        self.fields['proposal_title'].label = _('Your proposal\'s title')
        self.fields['proposal_abstract'].label = _('Abstract of your proposal')
        self.fields['proposal_audience'].label = _(
            'What\'s the intended audience of your proposal?')
        self.fields['workshop_duration'].lable = _('How long is the workshop?')
