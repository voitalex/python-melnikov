""" Выражение (612)

Даны N целых чисел X1, X2, ..., XN. Расставить между ними знаки "+" и "-" так, чтобы значение
получившегося выражения было равно заданному целому S.

Входные данные:
  * В первой строке находятся числа N и S.
  * В следующей строке - N чисел через пробел. 2 <= N <= 24, 0 <= Xi <= 50 000 000,
    -1 000 000 000 <= S <= 1 000 000 000.

Выходные данные:
  * Если получить требуемый результат невозможно, вывести "No solution", если можно, то вывести равенство.
  * Если решение не единственное, вывести любое.

Примеры :

Входные данные:
3 13
7 3 9
Выходные данные:
7-3+9=13

Входные данные:
3 1
7 3 9
Выходные данные:
7+3-9=1

Входные данные:
3 3
7 10 0
Выходные данные:
No solution
"""

from itertools import chain
from typing import Tuple


Ints = Tuple[int, ...]
Strings = Tuple[str, ...]


class FoundSolution(Exception):
    """ Исключение для выхода из рекурсивного стека в случае нахождения решения """


def solve_b(total: int, numbers: Ints) -> Strings:
    """ Возвращает все простые числа от M до N включительно """

    signs = [1] * len(numbers)

    def traverse(index: int, curr_sum: int):

        if index > 0:
            signs[index] = 1
            traverse(index - 1, curr_sum + numbers[index])
            signs[index] = -1
            traverse(index - 1, curr_sum - numbers[index])
        else:
            if curr_sum + numbers[0] == total:
                raise FoundSolution

    try:
        traverse(len(numbers) - 1, 0)
    except FoundSolution:
        return tuple({1: '+', -1: '-'}[x] for x in signs[1:])
    else:
        return tuple()


def main() -> None:
    """ Решение задачи """

    _, total = map(int, input().split(' '))
    numbers = tuple(map(int, input().split(' ')))

    signs = solve_b(total, numbers)
    if not signs:
        print('No solution')
        return

    expr = str(numbers[0]) + ''.join(map(str, chain.from_iterable(zip(signs, numbers[1:]))))
    print(f'{expr}={total}')


if __name__ == '__main__':
    main()
