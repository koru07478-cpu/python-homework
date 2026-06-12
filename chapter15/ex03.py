from chapter15.ex02 import *
from copy import deepcopy


def moved_rectangle(rect: Rectangle, dx: float, dy: float) -> Rectangle:
    """Принимает объект Rectangle и два числа dx и dy и возвращяет измененную копию (deepcopy) прямоугольника,
    прибавляя dx к координате x угла и dy к координате y.
    >>> box = create_rectangle(1, 2, 5, 6)
    >>> print_rectangle(moved_rectangle(box, 4, -4))
    (5, -2, 5, 6)
    """
    copy_rect = deepcopy(rect)
    copy_rect.corner.x += dx
    copy_rect.corner.y += dy
    return copy_rect