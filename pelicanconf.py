#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u'Business Solutions Hungary'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Budapest'

DEFAULT_LANG = u'hu'

#TAGS_SAVE_AS = ''
#TAG_SAVE_AS = ''
#PAGE_URL = 'pages/{slug}.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (('NAV', 'http://nav.gov.hu/'),
         ('Bérkalkulátor.org', 'http://www.hrportal.hu/index.phtml?page=berkalkulator_2016'),
         ('Jogszabályok', 'http://net.jogtar.hu/'))

# Social widget
SOCIAL = (('Partnerünk a R!PORT', 'http://riport.co.hu'),
	 )

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images']	
THEME = "./pelican-themes/bootstrap2"
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [ 'i18n_subsites']
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
	    ('Szolgáltatások','pages/services'),
	    ('Ajánlatkérés','pages/offer'),
	    ('Céginformációk','pages/info'),
	    ('Irodáink','pages/offices'),
	    ('Rólunk','pages/about_us'))

I18N_SUBSITES = {
    'de': {
        'SITENAME': 'nemet cím',
	},
    'en': {
        'SITENAME': 'angol ',
        },
    }

languages_lookup = {
    'hu': 'Magyar',
    'de': 'Deutsch',
    'en': 'English',
    }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def my_ordered_items(dict):
    items = list(dict.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'my_ordered_items': my_ordered_items,
    }

