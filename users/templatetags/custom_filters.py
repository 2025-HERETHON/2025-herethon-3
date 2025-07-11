# custom_filters.py
from django import template

register = template.Library()

@register.filter
def split_by_space(value):
    return value.split()


@register.filter
def split_plus(value):
    if value:
        return [s.strip() for s in value.split('+')]
    return []

@register.filter
def split_by_splash(value):
    if value:
        return [item.strip() for item in value.split('/')]
    return []

@register.filter
def split_by_comma(value):
    if value:
        return [item.strip() for item in value.split(',')]
    return []
