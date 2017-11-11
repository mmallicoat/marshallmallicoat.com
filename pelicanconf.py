AUTHOR = 'Marshall Mallicoat'
DEFAULT_LANG = 'en'
SITENAME = u'\u25B2' + u'HEAP'
PATH = 'content/'  # markup documents
TIMEZONE = 'America/New_York'

OUTPUT_PATH = 'output/'
# Maybe need to be careful with this
DELETE_OUTPUT_DIRECTORY = True

# https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
STATIC_PATHS = ['pages', 'media',
                'extra/robots.txt',
                'extra/sitemap.xml']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/sitemap.xml': {'path': 'sitemap.xml'},
}

# Wait to set until uploading site
# SITEURL = 'https://marshallmallicoat.com'
SITEURL = ''

# Try this later if you don't want to organize into subfolders
# USE_FOLDER_AS_CATEGORY = False

# Change location of pages to root directory, along with articles
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

THEME = 'mytheme'

# Atom/RSS Feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feed.xml'
