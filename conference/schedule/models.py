# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import datetime as dt

from autoslug import AutoSlugField
from autoslug.utils import slugify
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import truncatechars_html
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from filer.models import ThumbnailOption
from meta.models import ModelMeta

from conference.cfp.models import Submission, WorkshopSubmission


class Slot(ModelMeta, models.Model):
    """
    Model for conference time slots. It can be for a talk, a workshop, or a custom time slot (i. e. coffee break)
    """
    talk = models.ForeignKey(
        Submission, related_name='talks', limit_choices_to={'selected': True}, null=True, blank=True
    )
    slug = AutoSlugField(
        _('Slug'), max_length=400, blank=True, populate_from='generated_slug', always_update=True
    )
    workshop = models.ForeignKey(
        WorkshopSubmission, related_name='workshops', limit_choices_to={'selected': True}, null=True, blank=True
    )
    name = models.CharField(
        _('Name'), max_length=250, null=True, blank=True,
        help_text=_('Field for time slots that does not relate to a Talk or a Workshop.')
    )
    mugshot = FilerImageField(verbose_name=_('Speaker mughshot'), null=True, blank=True)
    twitter = models.CharField(_('Twitter'), max_length=200, default='', blank=True)
    schedule_abstract = models.TextField(_('Schedule abstract'), blank=True, null=True)
    day = models.DateField(_('Date'))
    start = models.TimeField(_('Start'))
    duration = models.DurationField(_('Duration'))
    sprint_days = models.BooleanField(_('Part of sprint days'), default=False)
    show_end_time = models.BooleanField(_('Show end time in schedule'), default=False)
    slides = models.URLField(_('Speaker slides'), blank=True, null=True)
    video = models.URLField(_('Talk video'), blank=True, null=True)

    _metadata = {
        'title': 'title',
        'description': 'get_meta_abstract',
        'image': 'get_image',
    }

    class Meta:
        verbose_name = _('Time slot')
        verbose_name_plural = _('Time slots')
        ordering = ('day', 'start')

    def clean(self):
        # ensure talk and workshop are NOT filled at the same time
        if self.talk and self.workshop:
            message = _('Please, select either a Talk or a Workshop, not both.')
            raise ValidationError({
                'talk': ValidationError(message=message, code='invalid'),
                'workshop': ValidationError(message=message, code='invalid'),
            })

    def get_image(self):
        if self.mugshot:
            return self.mugshot.url
        else:
            return None

    def get_meta_abstract(self):
        return truncatechars_html(self.abstract, 180)

    @property
    def title(self):
        if self.talk_id:
            return self.talk.proposal_title
        elif self.workshop_id:
            return self.workshop.proposal_title
        elif self.name:
            return self.name
        return ''

    @property
    def author(self):
        if self.talk:
            return self.talk.author
        elif self.workshop:
            return self.workshop.author
        return ''

    @property
    def generated_slug(self):
        return slugify(self.title)

    @property
    def twitter_split(self):
        if self.twitter:
            return self.twitter.split(',')
        return ''

    @property
    def abstract(self):
        if self.schedule_abstract:
            return self.schedule_abstract
        if self.talk:
            return self.talk.proposal_abstract
        elif self.workshop:
            return self.workshop.proposal_abstract
        return ''

    @property
    def bio(self):
        if self.is_talk() and self.talk.author_bio and len(self.talk.author_bio) > 3:
            return self.talk.author_bio
        if self.is_workshop() and self.workshop.author_bio and len(self.workshop.author_bio) > 3:
            return self.workshop.author_bio
        return ''

    @property
    def parsed_duration(self):
        minutes = self.duration.seconds//60
        hours = minutes//60
        if hours:
            minutes -= hours * 60
            if minutes:
                return '{}h {}min'.format(hours, minutes)
            return '{}h'.format(hours)
        return '{}min'.format(minutes)

    @property
    def end_time(self):
        combined = dt.datetime.combine(dt.date.today(), self.start)
        end_time = combined + self.duration
        return end_time.time()

    @property
    def height(self):
        return self.duration.total_seconds() / 100 * 6

    @property
    def thumbnail_option(self):
        return ThumbnailOption.objects.get(name__icontains='speaker').as_dict

    def is_talk(self):
        return True if self.talk else False
    is_talk.short_description = _('Talk')
    is_talk.boolean = True

    def is_workshop(self):
        return True if self.workshop else False
    is_workshop.short_description = _('Workshop')
    is_workshop.boolean = True

    def is_custom(self):
        return True if self.name else False
    is_custom.short_description = _('Custom')
    is_custom.boolean = True
