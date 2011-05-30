from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

# The base URL for the meetup API
BASE_URL = "https://api.meetup.com/"

# The API Key being used.
API_KEY = "5f29565e357337e6b607b71302b96d"

# Group being called.
GROUP_NAME = "lapython"

# Groups that could be called
GROUP_NAMES = ("lapython","ladjango","socalpython",)

# Fields to reconcile between a member and a group profile.
RECONCILE_FIELDS = (
    "additional",
    "bio",
    "comment",
    "created",
    "updated",        
    "name",
    "photo_url",
    "profile_url",
    "role",
    "site_url",
    "site_name",
    "status",
    "title"
)

cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': '/tmp/cache/data',
    'cache.lock_dir': '/tmp/cache/lock'
}

CACHE = CacheManager(**parse_cache_config_options(cache_opts))
