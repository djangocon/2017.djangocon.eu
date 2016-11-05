# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


class MailchimpPlugin(CMSPluginBase):
    name = _('Mailchimp Subscribe')
    render_template = 'helpers/mailchimp.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(MailchimpPlugin)
