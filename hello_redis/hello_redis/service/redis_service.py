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


def delete(key):
    return cache.delete(key)


def ttl(key):
    return cache.ttl(key)


# hash map
def h_get(key):
    return cache.hgetall(key)


def h_set(key, value_dict):
    return cache.hmset(key, value_dict)
