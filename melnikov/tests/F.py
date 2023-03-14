""" Покер (616) """

import pytest
from melnikov.problems.F import solve_f


@pytest.mark.f
@pytest.mark.parametrize(
    'a, expected',
    [
        ([13, 11, 3, 7, 1], 'Nothing'),
        ([8, 2, 7, 1, 12], 'Nothing'),
        ([5, 3, 1, 9, 3], 'One Pair'),
        ([4, 6, 6, 2, 2], 'Two Pairs'),
        ([6, 6, 6, 6, 6], 'Impossible'),
        ([1, 1, 1, 1, 2], 'Four of a Kind'),
        ([1, 1, 1, 2, 2], 'Full House'),
        ([3, 5, 4, 6, 7], 'Straight'),
        ([5, 5, 5, 6, 7], 'Three of a Kind'),
    ]
)
def test_solve_c(a, expected):
    assert solve_f(a) == expected
