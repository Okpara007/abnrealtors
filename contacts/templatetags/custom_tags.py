from django import template

register = template.Library()

@register.simple_tag
def increment(value=0):
    return value + 1