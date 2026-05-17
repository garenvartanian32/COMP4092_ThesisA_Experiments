from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def block_anyfilter(filter_func, *args, **kwargs):
    return filter_func(*args, **kwargs)