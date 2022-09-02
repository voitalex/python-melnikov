""" Треугольник и точка (614)

В декартовой системе координат на плоскости заданы координаты вершин треугольника и ещё одной точки.
Определить, принадлежит ли эта точка треугольнику.

Входные данные:
 * В четырёх строках находятся пары чисел - координаты точек.
 * Числа в первых трёх строках - это координаты вершин треугольника,
 * В четвёртой строке - координаты тестируемой точки.
 * Координаты вершин - целые числа, для любой точки выполняются следующие условия: -10 000 <= x, y <= 10 000.

Выходные данные:
 * Вывести слово "In", если точка находится внутри треугольника, или "Out" - если снаружи.

Примеры

Входные данные:
-2 -2
3 1
0 1
0 0
Выходные данные:
In

Входные данные:
-2 -2
3 1
0 1
2 -2
Выходные данные
Out
"""

from dataclasses import dataclass


@dataclass
class Point:
    """ Точка на плоскости """
    x: int
    y: int


@dataclass
class Triangle:
    """ Треугольник """
    a: Point
    b: Point
    c: Point


def sign(value: int) -> int:
    """ Возвращает знак числа """
    if value == 0:
        return 0
    return 1 if value > 0 else -1


def half_plane_sign(a: Point, b: Point, p: Point) -> int:
    """ Возвращает признак взаимного расположения точки p и прямой, проведенной через точки (a, b)

        Возвращает:
           +1 если точка p расположена в правой полуплоскости
           -1 если точка p расположена в левой полуплоскости
            0 если точка расположена на прямой
         None
    """
    return sign((p.x - a.x) * (b.y - a.y) - (p.y - a.y) * (b.x - a.x))


def on_line_segment(a: Point, b: Point, p: Point) -> bool:
    """ Возвращает True если точка p расположена на отрезке (a, b) """

    min_x, max_x = min(a.x, b.x), max(a.x, b.x)
    min_y, max_y = min(a.y, b.y), max(a.y, b.y)
    vector = (p.x - a.x) * (b.y - a.y) - (p.y - a.y) * (b.x - a.x)

    return (vector == 0) and (min_x <= p.x <= max_x) and (min_y <= p.y <= max_y)


def solve_d(triangle: Triangle, p: Point) -> bool:
    """ Возвращает True если точка находится внутри треугольника """

    ab_sign = half_plane_sign(triangle.a, triangle.b, p)
    bc_sign = half_plane_sign(triangle.b, triangle.c, p)
    ca_sign = half_plane_sign(triangle.c, triangle.a, p)

    # Точка лежит строго внутри треугольника
    inside = ab_sign != 0 and (ab_sign == bc_sign == ca_sign)

    # Точка лежит на границе треугольника
    on_border = on_line_segment(triangle.a, triangle.b, p) or \
                on_line_segment(triangle.b, triangle.c, p) or \
                on_line_segment(triangle.c, triangle.a, p)

    return inside or on_border


def main() -> None:
    """ Решение задачи """

    a = Point(*map(int, input().split(' ')))
    b = Point(*map(int, input().split(' ')))
    c = Point(*map(int, input().split(' ')))
    p = Point(*map(int, input().split(' ')))

    triangle = Triangle(a, b, c)

    result = solve_d(triangle, p)
    print('In' if result else 'Out')


if __name__ == '__main__':
    main()
