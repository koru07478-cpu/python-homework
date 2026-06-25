class Time:
    """Определяет время суток."""

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        """
        >>> print(Time(23, 59, 59).hour)
        23
        >>> print(Time(56, 10, 67).minute)
        Traceback (most recent call last):
        ValueError: Часы должны быть от 0 до 23
        >>> print(Time(20, 80).minute)
        Traceback (most recent call last):
        ValueError: Минуты должны быть от 0 до 59
        >>> print(Time(20, 10, 67).minute)
        Traceback (most recent call last):
        ValueError: Секунды должны быть от 0 до 59
        """
        Time.validate(hour, minute, second)

        self.hour = hour
        self.minute = minute
        self.second = second

    def validate(hour: int, minute: int, second: int) -> None:
        """Проверяет корректность времени в часах.

        >>> Time.validate(25, 0, 0)
        Traceback (most recent call last):
        ValueError: Часы должны быть от 0 до 23
        """
        if not (0 <= hour < 24):
            raise ValueError("Часы должны быть от 0 до 23")
        if not (0 <= minute < 60):
            raise ValueError("Минуты должны быть от 0 до 59")
        if not (0 <= second < 60):
            raise ValueError("Секунды должны быть от 0 до 59")

    def __str__(self):
        """
        >>> str(Time(1, 2, 3))
        '1:02:03'
        """
        return f"{self.hour}:{self.minute:02d}:{self.second:02d}"

    def __add__(self, other: Time | int) -> Time:
        """
        >>> print(Time(23, 2, 3) + Time(3, 2, 31) + 67)
        2:05:41
        >>> Time(1, 0, 0) + "1 час"
        Traceback (most recent call last):
        TypeError: объект other неподходящего типа
        """
        if isinstance(other, Time):
            return self.add_time(other)
        elif isinstance(other, int):
            return self.incremented(other)
        else:
            raise TypeError("объект other неподходящего типа")

    def __radd__(self, other: Time) -> Time:
        """
        >>> print(1 + Time(1, 2, 3) + Time(3, 2, 59))
        4:05:03
        """
        return self.__add__(other)

    def to_int(self) -> int:
        """Переводит время из типа Time в количество секунд, прошедших с полуночи.

        >>> Time(9, 0, 11).to_int()
        32411
        >>> Time(9).to_int()
        32400
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def add_time(self, other: Time) -> Time:
        """Прибавляет ко врмени время.

        >>> print(Time(23, 2, 3) + Time(4, 5, 6))
        3:07:09
        """
        seconds = self.to_int() + other.to_int()
        return int_to_time(seconds)

    def incremented(self, seconds: int) -> Time:
        """Прибавляет ко врмени секунды.

        >>> print(Time(20, 0, 10) + 36000)
        6:00:10
        """
        seconds += self.to_int()
        minutes, sec = divmod(seconds, 60)
        hour, min = divmod(minutes, 60)
        day, h = divmod(hour, 24)
        return Time(h, min, sec)

    def is_after(self, other: Time) -> bool:
        """Показывает, какое из двух времен идет позже другого.

        >>> Time(1, 2, 3).is_after(Time(1, 2, 2))
        True
        >>> Time(1, 2, 3).is_after(Time(1, 2, 3))
        False
        """
        return self.to_int() > other.to_int()


def int_to_time(seconds: int) -> Time:
    """Переводит количество секунд, прошедших с полуночи, в тип Time.

    >>> print(int_to_time(4948))
    1:22:28
    """
    minutes, sec = divmod(seconds, 60)
    hour, min = divmod(minutes, 60)
    day, h = divmod(hour, 24)
    return Time(h, min, sec)
