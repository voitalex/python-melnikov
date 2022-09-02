""" Простые числа (611) """

import pytest
from melnikov.problems.A import solve_a


@pytest.mark.a
@pytest.mark.parametrize(
    'm, n, expected',
    [
        (2, 5, [2, 3, 5]),
        (4, 4, []),
    ]
)
def test_solve_a(m, n, expected):
    assert list(solve_a(m, n)) == expected
