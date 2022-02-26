cache_dict = {}


def caching_decorator(use_cache=True):
    """
    Caching decorator, which have 'use_cache=True'
    parameter able to cache any function. If the result
    of this function is already calculated and in cache,
    cashing decorator return it from the cache. Otherwise
    (if no results, or decorator called with 'use_cache=False'),
    cashe decorator calculate the result, update the cache
    and return calculated value.
    """

    def my_use_cache(func):
        def wrapper(*args, **kwargs):
            if use_cache:
                key = f"{func.__name__} + {args}  {kwargs}"
                if key in cache_dict:
                    return cache_dict[key]
                cache_dict[key] = func(*args, **kwargs)
                return cache_dict[key]

            return func(*args, **kwargs)

        return wrapper

    return my_use_cache
