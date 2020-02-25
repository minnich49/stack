#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bob Minnich'
SITENAME = 'stack'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "pelican-bootstrap3"

IGNORE_FILES = [".ipynb_checkpoints"]  
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['pelican-plugins/i18n_subsites','./plugins']
PLUGINS = ['i18n_subsites','ipynb.markup']
PYGMENTS_STYLE = 'default'
BOOTSTRAP_THEME = 'Simplex'
BOOTSTRAP_THEME = 'Lumen'

BOOTSTRAP_FLUID = True
# Tell Pelican to add files from 'extra' to the output dir

CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add files from 'extra' to the output dir
STATIC_PATHS = [
  'extra/custom.css',
    'images'
]

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  
IPYNB_USE_METACELL = True

IPYNB_FIX_CSS = True

DISPLAY_BREADCRUMBS = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False