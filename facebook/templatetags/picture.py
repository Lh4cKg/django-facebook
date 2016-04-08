# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.simple_tag
def profile_picture(facebook_id):
    return "<img src=\'http://graph.facebook.com/%s/picture?type=%s\' alt=''/>" % (facebook_id, 'square')