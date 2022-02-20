import pytest

from hw2_Testing_Coverage.my_range import my_range


def test_my_range_one_number():
    assert list(my_range(10)) == list(range(10))


def test_my_range_zero():
    assert list(my_range(0)) == []


def test_my_range_step_two():
    assert list(my_range(0, 10, 2)) == list(range(0, 10, 2))


def test_my_range_step_two_reverse():
    assert list(my_range(10, 0, -2)) == list(range(10, 0, -2))


def test_my_range_reverse():
    assert list(my_range(0, -10, -2)) == list(range(0, -10, -2))


def test_my_range_type_error():
    with pytest.raises(AttributeError):
        my_range(0, 10, "qwer")


def test_my_range_value_error():
    with pytest.raises(ValueError):
        list(my_range(0, 10, 0))
