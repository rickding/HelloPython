from django.http import HttpResponse

from .service import redis_service as cache


def chk_cache(req):
    key = 'chk_cache: %s, %s, %s' % (req.get_raw_uri(), req.get_full_path(), req.get_host())
    value = cache.incr(key)
    cache.set(key, value * 2)

    return HttpResponse('cache, key: {}, value: {}'.format(key, cache.get(key)))
