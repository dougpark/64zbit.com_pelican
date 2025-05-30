# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://64zbit.com'

RELATIVE_URLS = False

# OUTPUT_PATH = 'publish'
FEED_ALL_JSON = 'feeds/all.json'
CATEGORY_FEED_JSON = 'feeds/%s.json'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "TRUE"