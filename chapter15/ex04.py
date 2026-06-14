from chapter15.point import *
from chapter15.ex02 import *
from math import sqrt


class Circle:
    """Определяет круг."""
    center: Point
    radius: float


def create_circle(x: float, y: float, radius: float) -> Circle:
    """Создает и возвращает объект Circle с заданными координатами и радиусом.
    >>> circ = create_circle(150, 100, 75)
    >>> isinstance(circ, Circle)
    True
    >>> circ.radius
    75
    >>> circ.center.x
    150
    >>> circ.center.y
    100
    """
    if radius <= 0:
        raise ValueError("Радиус должен быть больше нуля!")

    circ = Circle()
    circ.radius = radius
    circ.center = Point()
    circ.center.x = x
    circ.center.y = y
    return circ


my_circle = create_circle(150, 100, 75)


def point_in_on_circle(circle: Circle, point: Point) -> bool:
    """Принимает объекты Circle и Point и возвращает True, если точка лежит внутри круга или на его границе.
    >>> # Точка снаружи круга
    >>> point_in_on_circle(my_circle, create_point(40, 50))
    False
    >>> # Точка строго внутри круга
    >>> point_in_on_circle(my_circle, create_point(150, 100))
    True
    >>> # Точка ровно на границе круга
    >>> point_in_on_circle(my_circle, create_point(150, 175))
    True
    """
    dx = circle.center.x - point.x
    dy = circle.center.y - point.y
    if sqrt(dx**2 + dy**2) <= circle.radius:
        return True
    return False


def point_in_circle(circle: Circle, point: Point) -> bool:
    """Принимает объекты Circle и Point и возвращает True, если точка лежит внутри круга.
    >>> # Точка снаружи круга
    >>> point_in_circle(my_circle, create_point(40, 50))
    False
    >>> # Точка строго внутри круга
    >>> point_in_circle(my_circle, create_point(150, 100))
    True
    >>> # Точка ровно на границе круга
    >>> point_in_circle(my_circle, create_point(150, 175))
    False
    """
    dx = circle.center.x - point.x
    dy = circle.center.y - point.y
    if sqrt(dx**2 + dy**2) < circle.radius:
        return True
    return False


def rect_in_on_circle(circle: Circle, rectangle: Rectangle) -> bool:
    """Принимает объекты Circle и Rectangle и возвращает True, если прямоугольник полностью лежит внутри круга или на его границе.
    >>> # Прямоугольник частично снаружи круга
    >>> my_rectangle = create_rectangle(25, 35, 150, 100)
    >>> rect_in_on_circle(my_circle, my_rectangle)
    False

    >>> # Прямоугольник строго внутри круга
    >>> small_rect = create_rectangle(140, 90, 10, 10)
    >>> rect_in_on_circle(my_circle, small_rect)
    True

    >>> # Прямоугольник полностью снаружи круга
    >>> outside_rect = create_rectangle(0, 0, 10, 10)
    >>> rect_in_on_circle(my_circle, outside_rect)
    False

    >>> # Вписанный прямоугольник
    >>> border_rect = create_rectangle(105, 55, 90, 90)
    >>> rect_in_on_circle(my_circle, border_rect)
    True
    """
    point_right_down = create_point(rectangle.corner.x + rectangle.width, rectangle.corner.y)
    point_left_up = create_point(rectangle.corner.x, rectangle.corner.y + rectangle.height)
    point_diagonally = create_point(rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height)
    if point_in_on_circle(circle, rectangle.corner) and point_in_on_circle(circle, point_right_down) and point_in_on_circle(circle, point_left_up) and point_in_on_circle(circle, point_diagonally):
        return True
    return False


def rect_circle_overlap1(circle: Circle, rectangle: Rectangle) -> bool:
    """возвращает True, если любой угол прямоугольника находится внутри круга.
    >>> # Прямоугольник пересекает круг своими углами
    >>> my_rectangle = create_rectangle(25, 35, 150, 100)
    >>> rect_circle_overlap1(my_circle, my_rectangle)
    True

    >>> # Прямоугольник полностью снаружи, ни один угол не задевает круг
    >>> outside_rect = create_rectangle(0, 0, 10, 10)
    >>> rect_circle_overlap1(my_circle, outside_rect)
    False

    >>> # Один из углов прямоугольника касается ровно линии границы круга. (Тут не говорилось, что мы границу круга принимаем за его внтуренность, поэтому выводим False)
    >>> touching_corner_rect = create_rectangle(150, 175, 20, 20)
    >>> rect_circle_overlap1(my_circle, touching_corner_rect)
    False

    >>> # Круг пронзает сторону прямоугольника, но все углы снаружи
    >>> side_pierce_rect = create_rectangle(140, 0, 20, 200)
    >>> rect_circle_overlap1(my_circle, side_pierce_rect)
    False
    """
    point_right_down = create_point(rectangle.corner.x + rectangle.width, rectangle.corner.y)
    point_left_up = create_point(rectangle.corner.x, rectangle.corner.y + rectangle.height)
    point_diagonally = create_point(rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height)
    if point_in_circle(circle, rectangle.corner) or point_in_circle(circle, point_right_down) or point_in_circle(circle, point_left_up) or point_in_circle(circle, point_diagonally):
        return True
    return False


def rect_circle_overlap2(circle: Circle, rectangle: Rectangle) -> bool:
    """Вернет True, если любая часть прямоугольника пересекается с кругом.
    >>> # Прямоугольник пересекает круг углами
    >>> rect_circle_overlap2(my_circle, create_rectangle(25, 35, 150, 100))
    True
    >>> # Прямоугольник олностью снаружи круга
    >>> rect_circle_overlap2(my_circle, create_rectangle(0, 0, 10, 10))
    False
    >>> # Круг пересекает только сторону прямоугольника
    >>> rect_circle_overlap2(my_circle, create_rectangle(140, 0, 20, 200))
    True
    >>> # Круг полностью внутри прямоугольника
    >>> rect_circle_overlap2(my_circle, create_rectangle(50, 0, 300, 300))
    True
    """
    point_right_down = create_point(rectangle.corner.x + rectangle.width, rectangle.corner.y)
    point_left_up = create_point(rectangle.corner.x, rectangle.corner.y + rectangle.height)

    if circle.center.x - circle.radius <= max(rectangle.corner.x, min(circle.center.x,point_right_down.x)) <= circle.center.x + circle.radius and (rectangle.corner.y <= circle.center.y <= point_left_up.y):
        return True
    elif circle.center.y - circle.radius <= max(rectangle.corner.y, min(circle.center.y,point_left_up.y)) <= circle.center.y + circle.radius and (rectangle.corner.x <= circle.center.x <= point_right_down.x):
        return True
    elif rect_circle_overlap1(circle, rectangle):
        return True
    else:
        return False




