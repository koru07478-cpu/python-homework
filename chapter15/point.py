from math import sqrt
from chapter15.ex01 import Point


def create_point(x: float, y: float) -> Point:
    """Создать Point с координатами (x, y).
    >>> p = create_point(1, 2)
    >>> p.x
    1
    >>> p.y
    2
    """
    p = Point()
    p.x = x
    p.y = y
    return p

def distance_between_points(p1: Point, p2: Point) -> float:
   """Возвращает расстояние между точками p1 и p2.
   >>> distance_between_points(create_point(0, 0), create_point(3, 4))
   5.0
   """
   dx = p2.x - p1.x
   dy = p2.y - p1.y
   return sqrt(dx**2 + dy**2)
