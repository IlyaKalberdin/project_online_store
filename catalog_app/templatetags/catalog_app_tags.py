from django import template
from os.path import join


register = template.Library()


@register.filter(needs_autoescape=True)
def mediapath(path, autoescape=True):
    if autoescape:
        return join('media', path)


@register.simple_tag
def mediapath(path):
    return join('media', path)
