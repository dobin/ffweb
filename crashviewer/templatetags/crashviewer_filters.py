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

    if len(value) > 64:
        value = value[:64]
        value = hexdump.dump(value)
        value += " .."
    else:
        value = hexdump.dump(value)

    return value


@register.filter(name='filenameof')
def filenameof(value):
    return os.path.basename(value)


@register.filter(name='shortseed')
def shortseed(value):
    return value[:6]
