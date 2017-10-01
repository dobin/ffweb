from django import template
from datetime import date, timedelta
import os
import hexdump
import base64

register = template.Library()


@register.filter(name='myhex')
def myhex(value):
    return hex(value)


@register.filter(name='myhexblong')
def myhexblong(value):
    value = base64.b64decode(value)
    return hexdump.dump(value)



@register.filter(name='filenameof')
def filenameof(value):
    return os.path.basename(value)


@register.filter(name='shortseed')
def shortseed(value):
    return value[:6]
