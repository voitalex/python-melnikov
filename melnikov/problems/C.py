""" Возрастающая подпоследовательность (613)

Даны N целых чисел X1, X2, ..., Xn. Требуется вычеркнуть из них минимальное количество чисел так,
чтобы оставшиеся шли в порядке возрастания.

Входные данные:
 * В первой строке находится число N.
 * В следующей строке - N чисел через пробел. 1 <= N <= 10 000, 1 <= Xi <= 60 000.

Выходные данные:
 * В первой строке выводится количество невычеркнутых чисел.
 * Во второй - сами невычеркнутые числа через пробел в исходном порядке.
 * Если вариантов несколько, вывести любой.

Примеры:

Входные данные:
5
1 3 5 2 4

Выходные данные:
3
1 3 5
"""

from itertools import islice, chain
from typing import List


def solve_c(numbers: List[int]) -> List[int]:
    """ Возвращает максимальную последовательность возрастающих чисел """

    lengths: List[int] = [0] * len(numbers)

    # Для каждого члена исходной последовательности вычисляем максимальную длину
    # возрастающей подпоследовательности, оканчивающейся этим элементом и сохраняем
    # в массиве lengths.

    #  Пусть известны максимальную длины для всех членов последовательности от 0-го до (i - 1)-гo
    #  и нужно узнать ее для i-ro. Последовательность длиной 1 из одного (i-гo) элемента всегда
    #  можно построить. Пусть можно построить последовательность длиной не меньше двух.
    #  Тогда какой-то из элементов от 0-го до (i - 1)-гo будет предпоследним. Очевидно,
    #  что предпоследним может быть любой элемент, меньший i-гo. А наилучшая характеристика
    #  у i-го элемента получится, если взять предыдущий элемент с максимальной характеристикой.

    max_length, max_length_index = 0, 0
    for o_index, o_num in enumerate(numbers):

        num_lengths = zip(islice(numbers, 0, o_index), islice(lengths, 0, o_index))
        lengths[o_index] = max(chain((length for num, length in num_lengths if num < o_num), [0])) + 1
        if max_length <= lengths[o_index]:
            max_length, max_length_index = lengths[o_index], o_index

    # Восстанавливаем элементы максимальной возрастающей подпоследовательности
    result = [numbers[max_length_index]]
    prev_index = max_length_index
    for index in range(max_length_index - 1, -1, -1):
        if numbers[index] < numbers[prev_index] and lengths[index] == lengths[prev_index] - 1:
            prev_index = index
            result.append(numbers[index])

    result.reverse()

    return result


def main() -> None:
    """ Решение задачи """

    _ = int(input())
    numbers = list(map(int, input().split(' ')))

    result = solve_c(numbers)

    print(len(result))
    print(' '.join(str(x) for x in result))


if __name__ == '__main__':
    main()
