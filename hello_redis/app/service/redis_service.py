from django.core.cache import cache


def incr(key, amount=1):
    if cache.has_key(key):
        return cache.incr(key, amount)

    cache.set(key, amount)
    return amount


def get(key):
    return cache.get(key)


def set(key, value):
    return cache.set(key, value)
