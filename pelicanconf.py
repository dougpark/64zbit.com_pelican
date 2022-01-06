AUTHOR = 'Doug'
SITENAME = '64Zbit.com'
SITESUBTITLE = 'Tech is way, WAY interesting'
# SITEURL = 'https://dev.64zbit.com'
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = True
SITEYEAR = '2022'

PATH = 'content'
OUTPUT_PATH = 'output'

THEME = './dnp-aboutwilson'
#THEME = './pelican-simplegrey'
#THEME = './pelican-svbhack-master'
#THEME = './pelican-themes/pelican-themes/backdrop'
 

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# PLUGIN_PATHS = ['voce/plugins']
# PLUGINS = ['assets']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
MENUITEMS = (('Contact', '/pages/contact.html'),
         ('Archive', '/archives.html'),
         ('Authors', '/authors.html'),
         ('Categories', '/categories.html'),
         ('Tags', '/tags.html'),)

LINKS = (('GitHub', 'https://github.com/dougpark'),)
         

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/64zbit'),)
           
# SOCIAL = (('Doug', 'https://twitter.com/64zbit'),
#            ('social-2', '#'),)

DEFAULT_PAGINATION = 25
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True