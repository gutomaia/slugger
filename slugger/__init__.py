# -*- coding: utf-8 -*-

from string import replace
from re import match, sub

def slugify(param):
    name = param.lower()
    name = sub(ur'[- ]', '_', name)
    name = sub(ur'[à-ä]', 'a', name)
    name = sub(ur'[è-ë]', 'e', name)
    name = sub(ur'[ì-ï]', 'i', name)
    name = sub(ur'[ò-ö]', 'o', name)
    name = sub(ur'[ù-ü]', 'u', name)
    name = replace(name, u'ç', 'c')
    name = sub(r'[^a-z0-9_]+','?',name)
    m = match(r'^([a-z0-9_]+)$', name)
    if m is not None:
        return name
    raise Exception('Could not slugify this: %s' % param)
