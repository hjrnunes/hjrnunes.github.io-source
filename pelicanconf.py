#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Henrique'
SITENAME = u'Ultramar'
SITESUBTITLE = u'Polemos Pyrinos'
SITEURL = ''
TYPOGRIFY = True

TIMEZONE = 'Europe/London'

DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'pt': ('pt_PT','aos %d de %B de %Y'),
}

THEME = 'pageturner-pelican'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = [
    ('Blog','/'),
    ('Archives','/'),
]

PLUGIN_PATH = "plugins"
PLUGINS = ['optimize_images', 'summary', 'post_stats']