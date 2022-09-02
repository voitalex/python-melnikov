""" Возрастающая подпоследовательность (613) """


import pytest
from melnikov.problems.C import solve_c


@pytest.mark.c
@pytest.mark.parametrize(
    'numbers, expected',
    [
        ([1, 3, 5, 2, 4], [1, 2, 4]),
        ([4, 4], [4]),
    ]
)
def test_solve_c(numbers, expected):
    assert solve_c(numbers) == expected
