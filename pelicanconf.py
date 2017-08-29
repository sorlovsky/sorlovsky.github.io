#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Simon Orlovsky'
SITENAME = u'Piegenstuff'
SITEURL = ''

PATH = 'content'
SITESUBTITLE ='Mostly python and math stuff'
SITETAG = "Piegenstuff"


TIMEZONE = 'America/Los_Angeles'    

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (('Dormcuts in USA Today', 'http://college.usatoday.com/2015/10/17/dorm-hair-cuts/'),
         ('Dancing with the Stars', 'https://www.youtube.com/watch?v=Dpy_5Hy0zv8'))

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SOCIAL = (('Twitter', 'https://twitter.com/simonthebarber',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin.com/in/simonorlovsky',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/sorlovsky',
         'fa fa-github-square fa-fw fa-lg'),
        )


DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = 'voidy-bootstrap'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
