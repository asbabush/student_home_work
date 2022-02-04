import pytest

from hw0_intro.main import mul


def test_mul_positive_number():
    assert mul(1, 2) == 2


def test_mul_zero_number():
    assert mul(2, 0) == 0


def test_raise_type_error():
    with pytest.raises(TypeError):
        mul("a", "b")
