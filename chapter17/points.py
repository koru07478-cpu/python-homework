class Point:
    """Представление точки в двумерном пространстве."""

    def __init__(self, x: float = 0, y: float = 0):
        """
        >>> print(f"x: {Point(12, 23).x}, y: {Point(12, 23).y}")
        x: 12, y: 23
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        >>> str(Point(12, 23))
        '(12; 23)'
        """
        return f"({self.x}; {self.y})"

    def __add__(self, other: Point | tuple) -> Point:
        """
        >>> print(Point(1, 2) + Point(4, 3))
        (5; 5)
        >>> print(Point(1, 2) + (4, 3))
        (5; 5)
        >>> print(Point(1, 2) + (4, 3) + Point(4, 3) + (1, 2))
        (10; 10)
        >>> print(Point(4, 3) + "точка (1;2)")
        Traceback (most recent call last):
        TypeError: объект other неподходящего типа
        """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("объект other неподходящего типа")

    def __radd__(self, other: tuple) -> Point:
        """
        >>> print((4, 3) + Point(4, 3))
        (8; 6)
        >>> print((4, 3) + Point(4, 3) + Point(1, 2) + (4, 3))
        (13; 11)
        """
        return self.__add__(other)
