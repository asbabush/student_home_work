import pytest

from hw2_Testing_Coverage.caching_decorator import (cache_dict,
                                                    caching_decorator)


@caching_decorator(True)
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@caching_decorator(False)
def my_sum(a, b):
    return a + b


def test_caching_decorator_use_dict():
    fibonacci(10)
    assert cache_dict["fibonacci + (6,)  {}"] == 8


def test_caching_decorator_not_use_dict():
    my_sum(123, 127)
    with pytest.raises(KeyError):
        test_var = cache_dict["my_sum + (123, 127)  {}"]
