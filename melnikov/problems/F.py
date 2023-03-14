""" Покер (616)

Даны 5 целых чисел. Среди них:
 * если одинаковы 5, то вывести "Impossible", иначе
 * если одинаковы 4, то вывести "Four of a Kind", иначе
 * если одинаковы 3 и 2, то вывести "Full House", иначе
 * если есть 5 последовательных, то вывести "Straight", иначе
 * если одинаковы 3, то вывести "Three of a Kind", иначе
 * если одинаковы 2 и 2, то вывести "Two Pairs", иначе
 * если одинаковы 2, то вывести "One Pair", иначе
 * вывести "Nothing".

Входные данные:
 * В первой строке находятся 5 чисел через пробел. Все числа от 1 до 13 включительно.

Выходные данные:
 * Выводится одна строка - результат анализа.

Примеры:

Входные данные:
13 11 3 7 1
Выходные данные:
Nothing

Входные данные:
8 2 7 1 12
Выходные данные:
Nothing

Входные данные:
5 3 1 9 3
Выходные данные:
One Pair

Входные данные:
4 6 6 2 2
Выходные данные:
Two Pairs
"""

from collections import Counter
from typing import Optional, List


def solve_f(numbers: List[int]) -> str:
    """ Возвращает название карточной комбинации """

    def impossible() -> Optional[str]:
        """ Возвращает Impossible если у игрока пять одинаковых карт """
        return 'Impossible' if set(counter.values()) == {number_of_cards} else None

    def four_of_a_kind() -> Optional[str]:
        """ Возвращает Four of a Kind если у игрока четыре одинаковые карты """
        return 'Four of a Kind' if 4 in set(counter.values()) else None

    def full_house() -> Optional[str]:
        """ Возвращает Full House если у игрока две и три одинаковые карты """
        return 'Full House' if set(counter.values()) == {2, 3} else None

    def straight() -> Optional[str]:
        """ Возвращает Straight если у игрока пять последовательных карт """
        min_card, max_card = min(counter), max(counter)
        if len(counter) == number_of_cards and max_card - min_card == number_of_cards - 1:
            return 'Straight'
        return None

    def three_of_a_kind() -> Optional[str]:
        """ Возвращает Three of a Kind если у игрока три одинаковые карты """
        return 'Three of a Kind' if 3 in set(counter.values()) else None

    def two_pairs() -> Optional[str]:
        """ Возвращает Two Pairs если у игрока две пары одинаковых карт """
        value_counter = Counter(counter.values())
        return 'Two Pairs' if 2 in set(value_counter.values()) else None

    def one_pair() -> Optional[str]:
        """ Возвращает One Pair если у игрока одна пара одинаковых карт """
        return 'One Pair' if 2 in set(counter.values()) else None

    def nothing() -> str:
        """ Возвращает значение по умолчанию если у игрока нет комбинации из карт """
        return 'Nothing'

    number_of_cards = len(numbers)
    counter = Counter(numbers)

    for check in (impossible, four_of_a_kind, full_house, straight, three_of_a_kind, two_pairs, one_pair):
        if result := check():
            return result

    return nothing()

def main() -> None:
    """ Решение задачи """

    numbers = list(map(int, input().split(' ')))
    print(solve_f(numbers))


if __name__ == '__main__':
    main()