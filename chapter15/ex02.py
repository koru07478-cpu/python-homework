from chapter15.ex01 import Point


class Rectangle:
    """Определяет прямоугольник."""
    corner: Point
    width: float
    height: float


def create_rectangle(corner_x: float, corner_y: float, width: float, height: float) -> Rectangle:
    """Создать Rectangle с шириной, высотой и координатами угла.
    >>> rec = create_rectangle(1, 2, 5, 6)
    >>> rec.width
    5
    >>> rec.height
    6
    >>> rec.corner.x
    1
    >>> rec.corner.y
    2

    >>> create_rectangle(5, 2, 0, 6)
    Traceback (most recent call last):
    ValueError: Ширина и высота должны быть больше нуля!
    """
    if width <= 0 or height <= 0:
        raise ValueError("Ширина и высота должны быть больше нуля!")

    box = Rectangle()
    box.width = width
    box.height = height
    box.corner = Point()
    box.corner.x = corner_x
    box.corner.y = corner_y
    return box


def print_rectangle(rect: Rectangle) -> None:
    """Вывести Rectangle на экран
    >>> print_rectangle(create_rectangle(1, 2, 5, 6))
    (1, 2, 5, 6)
    """
    print(f'({rect.corner.x}, {rect.corner.y}, {rect.width}, {rect.height})')


def move_rectangle(rect: Rectangle, dx: float, dy: float) -> None:
    """Принимает объект Rectangle и два числа dx и dy и изменяет положение прямоугольника,
    прибавляя dx к координате x угла и dy к координате y.
    >>> box = create_rectangle(1, 2, 5, 6)
    >>> move_rectangle(box, 4, -4)
    >>> print_rectangle(box)
    (5, -2, 5, 6)
    """
    rect.corner.x += dx
    rect.corner.y += dy
