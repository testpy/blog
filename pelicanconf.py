#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'testpy team'
SITENAME = u'testpy'
SITEURL = 'http://localhost:8000'
TAGLINE = 'Software Testing and more'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/CNAME']

THEME = "theme/pure/"
COVER_IMG_URL = "http://i.imgur.com/rdpkAUi.jpg"
PLUGIN_PATH = "pelican-plugins/"
PLUGINS = ['gravatar']
DISQUS_SITENAME = "testpy"
GOOGLE_ANALYTICS = "UA-44297043-1"

MENUITEMS = [('Archive', 'archives.html'), ('About', 'about-us.html'), ]
SOCIAL = (('Github', 'https://github.com/testpy/'), )
DISPLAY_PAGES_ON_MENU = False

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
