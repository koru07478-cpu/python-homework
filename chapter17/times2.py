class Time:
    """Определяет время суток в секундах, прошедших с полуночи."""

    def validate(sec: int, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        """Проверяет корректность времени в часах.

        >>> Time.validate(90000)
        Traceback (most recent call last):
        ValueError: Секунды должны быть от 0 до 86399
        """
        if not (0 <= hour < 24):
            raise ValueError("Часы должны быть от 0 до 23")
        if not (0 <= minute < 60):
            raise ValueError("Минуты должны быть от 0 до 59")
        if not (0 <= second < 60):
            raise ValueError("Секунды должны быть от 0 до 59")
        if not (0 <= sec < 86400):
            raise ValueError("Секунды должны быть от 0 до 86399")

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
        self.hour = hour
        self.minute = minute
        self.second = second

        min = hour * 60 + minute
        sec = min * 60 + second
        Time.validate(sec, hour, minute, second)
        self.sec = sec

    def __str__(self):
        """
        >>> str(Time(1, 2, 3))
        '3723'
        """
        return f"{self.sec:02d}"

    def __add__(self, other: Time | int) -> Time | int:
        """
        >>> print(Time(23, 2, 3) + Time(3, 2, 31) + 67)
        7541
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

    def __radd__(self, other: Time) -> Time | int:
        """
        >>> print(1 + Time(1, 2, 3) + Time(3, 2, 59))
        14703
        """
        return self.__add__(other)

    def to_time(self) -> Time:
        """Переводит количество секунд, прошедших с полуночи, в тип Time.

        >>> print(Time(1, 22, 28).to_time())
        4948
        """
        minutes, sec = divmod(self.sec, 60)
        hour, min = divmod(minutes, 60)
        day, h = divmod(hour, 24)
        return Time(h, min, sec)

    def add_time(self, other: Time) -> int:
        """Прибавляет ко врмени время.

        >>> print(Time(23, 2, 3) + Time(4, 5, 6))
        11229
        """
        return (self.sec + Time(other.hour, other.minute, other.second).sec) % 86400

    def incremented(self, seconds: int) -> int:
        """Прибавляет ко врмени секунды.

        >>> print(Time(20, 0, 10) + 36000)
        21610
        """
        return (self.sec + seconds) % 86400

    def is_after(self, other: Time) -> bool:
        """Показывает, какое из двух времен идет позже другого.

        >>> Time(1, 2, 3).is_after(Time(1, 2, 2))
        True
        >>> Time(1, 2, 3).is_after(Time(1, 2, 3))
        False
        """
        return self.sec > Time(other.hour, other.minute, other.second).sec
