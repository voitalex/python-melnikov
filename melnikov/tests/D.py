""" Треугольник и точка (614) """

import pytest
from melnikov.problems.D import solve_d, Triangle, Point


@pytest.mark.d
@pytest.mark.parametrize(
    'triangle, point, expected',
    [
        (Triangle(Point(-2, -2), Point(3, 1), Point(0, 1)), Point(0, 0), True),
        (Triangle(Point(-2, -2), Point(3, 1), Point(0, 1)), Point(2, -2), False),
        (Triangle(Point(-2, -2), Point(3, 1), Point(0, 1)), Point(0, 1), True),
        (Triangle(Point(-2, -2), Point(3, 1), Point(0, 1)), Point(-2, 1), False),
        (Triangle(Point(-2000, -2000), Point(1000, 3000), Point(1000, 0)), Point(1000, -2000), False),
    ]
)
def test_solve_c(triangle, point, expected):
    assert solve_d(triangle, point) == expected
