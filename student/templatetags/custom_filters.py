# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def char(value, length=10):
    """এটি স্ট্রিংয়ের প্রথম 'length' অক্ষর বের করবে"""
    if isinstance(value, str):
        return value[:length]
    return value
