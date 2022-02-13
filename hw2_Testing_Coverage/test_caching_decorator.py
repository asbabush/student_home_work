import pytest

from hw2_Testing_Coverage.caching_decorator import (cache_dict,
                                                    caching_decorator)


def test_caching_decorator_use_dict():
    @caching_decorator(True)
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    @caching_decorator(False)
    def my_fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(6)

    assert my_fibonacci(6) == cache_dict["fibonacci + (6,)  {}"]


def test_caching_decorator_use_cache_false():
    @caching_decorator(False)
    def my_sum(a, b):
        return a + b

    cache_dict = {}
    my_sum(2, 2)
    assert cache_dict == {}


def test_caching_decorator_use_cache_true():
    @caching_decorator(True)
    def my_sum(a, b):
        return a + b

    my_sum(2, 2)
    assert cache_dict["my_sum + (2, 2)  {}"] == 4
