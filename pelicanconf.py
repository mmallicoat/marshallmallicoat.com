AUTHOR = 'Marshall Mallicoat'
DEFAULT_LANG = 'en'
SITENAME = u'\u25B2' + u'HEAP'  # code point for triangle
PATH = 'content/'  # markup documents
TIMEZONE = 'America/Chicago'

OUTPUT_PATH = 'output/'
# Delete files on rebuild except for selected ones
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", "README.rst", "CNAME"]

# Use extra/ paths for copying over robots.txt and sitemap.xml
# See: https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
STATIC_PATHS = ['pages', 'media',
                'html', 'data', 'figures',
                'extra/robots.txt',
                'extra/sitemap.xml'
                ]
# These paths will not be parsed as markup into HTML
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/sitemap.xml': {'path': 'sitemap.xml'},
    'html': {'path': 'html'}
    }
# Do not process these folders as articles
ARTICLE_EXCLUDES = ['html']

# Set to 'mm.com' before uploading; use '' when testing.
# SITEURL = 'http://marshallmallicoat.com'
SITEURL = ''

# Change location of pages to root directory, along with articles
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Name of CSS theme to use
THEME = 'mytheme'

# Atom/RSS Feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feed.xml'
