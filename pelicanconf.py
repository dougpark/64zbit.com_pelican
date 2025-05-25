from datetime import date

CURRENTYEAR = date.today().year
AUTHOR = 'Doug'
SITENAME = '64Zbit.com'
SITESUBTITLE = 'Tech is way, WAY interesting'

SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False
SITEYEAR = CURRENTYEAR  

STATIC_PATHS = ['Projects']

# LOAD_CONTENT_CACHE = False

PATH = 'content'
OUTPUT_PATH = 'output'

# THEME = './dnp-aboutwilson'
THEME = './dnp-w3css'
#THEME = './pelican-svbhack-master'
#THEME = './pelican-themes/pelican-themes/backdrop'
 
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['./plugins']
# https://github.com/andrewheiss/pelican_json_feed
PLUGINS = ['pelican_json_feed']

# Feed generation is usually not desired when developing
FEED_ALL_JSON = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAG_CLOUD_STEPS = 4         # Number of different sizes
TAG_CLOUD_MAX_ITEMS = 100   # Max tags to show

# DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']

# Navigation
# ('Contact', '/pages/contact.html'),
#  ('Authors', '/authors.html'),
# ('Tags', '/tags.html')
MENUITEMS = (('Archive', '/archives.html'),
        
                ('Categories', '/categories.html'),
            )

LINKS = (('Play Pluto Attacks','https://povingames.com/plutoattacks/'),

        )
         
 
# Social widget
SOCIAL = (('@64zbit', 'https://twitter.com/64zbit'),
          ('@GetPelican', 'https://twitter.com/getpelican'),
          ('@Phaser.io','https://twitter.com/phaser_')
          )
           
# SOCIAL = (('Doug', 'https://twitter.com/64zbit'),
#            ('social-2', '#'),)

DEFAULT_PAGINATION = 25
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True