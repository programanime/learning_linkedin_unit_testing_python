from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7212, 17.2212)
    assert p1.get_location() == (14.7212, 17.2212)


def test_invalid_point_generation():
    with pytest.raises(Exception) as exp:
        Point("Bogota", 12.32132, -10000)
    assert str(exp.value) == "Invalid latitude or longitude"


def test_invalid_name():
    with pytest.raises(Exception) as exp:
        Point(1, 12.32132, 12.31321)
    assert str(exp.value) == "Name must be a string"
