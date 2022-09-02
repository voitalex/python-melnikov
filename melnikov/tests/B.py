""" Выражение (612) """

import pytest
from melnikov.problems.B import solve_b

@pytest.mark.b
@pytest.mark.parametrize(
    'total, numbers, expected',
    [
        (3, (7, 10, 0), ()),
        (13, (7, 3, 9), ('-', '+')),
        (0, (1, 1, 1, 1), ('-', '-', '+')),
        (1, (7, 3, 9), ('+', '-')),
        (
            -80507031,
            (8593682, 31716735, 21491280, 17902794, 33317802, 31903797, 43140236, 27960611, 49962940, 89871,
             21765518, 824859, 10008534, 49081942, 37138133, 10339902, 46783173, 45482021, 19050964, 36953244,
             15710201, 13017280, 32752188, 4020978),
            ('+', '-', '-', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+', '+', '-', '+', '-', '-', '+',
             '-', '-', '-', '+'),
        ),
    ]
)
def test_solve_b(total, numbers, expected):
    assert solve_b(total, numbers) == expected
