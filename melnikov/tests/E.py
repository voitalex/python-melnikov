""" Степень (615) """

import pytest
from melnikov.problems.E import solve_e


@pytest.mark.e
@pytest.mark.parametrize(
    'a, n, expected',
    [
        (1, 1, 1),
        (1, 8000, 1),
        (3, 3, 27)
    ]
)
def test_solve_c(a, n, expected):
    assert solve_e(a, n) == expected
