from django import template
from datetime import date, timedelta
import os

register = template.Library()


@register.filter(name='myhex')
def myhex(value):
    return hex(value)


@register.filter(name='filenameof')
def filenameof(value):
    return os.path.basename(value)
