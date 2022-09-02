""" Простые числа (611)

Вывести все простые числа от M до N включительно.

Входные данные:
 * В первой строке находятся разделённые пробелом M и N. 2 <= M <= N <= 300 000.

Выходные данные:
 * Вывести числа в порядке возрастания, по одному в строке.
 * Если между M и N включительно нет простых - вывести "Absent".

Примеры:

Входные данные:
2 5
Выходные данные:
2
3
5

Входные данные:
4 4
Выходные данные:
Absent
"""

import math
from typing import Iterable


def solve_a(left: int, right: int) -> Iterable[int]:
    """ Возвращает все простые числа от M до N включительно """

    for number in range(left, right + 1):

        square_of_number = int(math.sqrt(number))
        for factor in range(2, square_of_number + 1):
            if number % factor == 0:
                break
        else:
            yield number


def main() -> None:
    """ Решение задачи """

    m, n = map(int, input().split(' '))

    prime_numbers = list(solve_a(m, n))
    if prime_numbers:
        print('\n'.join(str(x) for x in prime_numbers))
    else:
        print('Absent')


if __name__ == '__main__':
    main()
