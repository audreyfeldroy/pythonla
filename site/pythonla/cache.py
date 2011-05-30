from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': '/tmp/cache/data',
    'cache.lock_dir': '/tmp/cache/lock'
}

bcache = CacheManager(**parse_cache_config_options(cache_opts))

from meetup_api.meetup import Meetup
meetup = Meetup()

@bcache.cache('get_events_func', expire=1800)
def get_events():
    return meetup.get_events()


@bcache.cache('get_full_profiles_func', expire=1800)
def get_full_profiles():
    return meetup.get_full_profiles()

