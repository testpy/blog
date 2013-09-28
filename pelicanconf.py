#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'testpy team'
SITENAME = u'testpy'
SITEURL = 'http://testpy.org'
TAGLINE = 'Software Testing and more'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = u'en'

FEED_ALL_RSS = "feeds/all.rss.xml"
TAG_FEED_RSS = "feeds/%s.rss.xml"

FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/%s.atom.xml"

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['images', 'extra/CNAME']

THEME = "theme/pure/"
COVER_IMG_URL = "https://d233eq3e3p3cv0.cloudfront.net/max/1000/0*QSJkV5TP-AvgBz0M.gif"
PLUGIN_PATH = "pelican-plugins/"
PLUGINS = ['gravatar']
DISQUS_SITENAME = "testpy"
GOOGLE_ANALYTICS = "UA-44297043-1"

MENUITEMS = [('About', 'about-us.html'), ]
SOCIAL = (('Github', 'https://github.com/testpy/'), )
DISPLAY_PAGES_ON_MENU = False

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
