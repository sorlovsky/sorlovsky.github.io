#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Simon Orlovsky'
SITENAME = 'Data Science and Software Engineering'
SITEURL = ''
#THEME = 'pelican-themes/pelican-bootstrap3/'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (('Dormcuts in USA Today', 'http://college.usatoday.com/2015/10/17/dorm-hair-cuts/'),
         ('Dancing with the Stars', 'https://www.youtube.com/watch?v=Dpy_5Hy0zv8'))

# Social widget
SOCIAL = (('Instagram', 'http://instagram.com/simonorlovsky'),
          ('LinkedIn', 'http://linkedin.com/in/simonorlovsky'),)

DEFAULT_PAGINATION = 10
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
