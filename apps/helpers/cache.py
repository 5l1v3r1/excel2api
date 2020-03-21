from functools import wraps

from cachetools import TTLCache

cache_ttl = TTLCache(maxsize=10_000, ttl=360)


def cache_data(f):
    @wraps(f)
    def cache(*args, **kwargs):
        __cache_name = '{}-{}'.format(f.__name__, ",".join([i for i in args]))
        if cache_ttl.get(__cache_name, None) is None:
            cache_ttl[__cache_name] = f(*args, **kwargs)

        return cache_ttl[__cache_name]

    return cache
