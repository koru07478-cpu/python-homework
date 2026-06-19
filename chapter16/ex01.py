class Time:
    """Определяет время суток."""

    hour: int
    minute: int
    second: int


def print_time(time: Time) -> None:
    """Принимает объект Time и печатает его в форме hour:minute:second.
    >>> time1 = Time()
    >>> time1.hour = 11
    >>> time1.minute = 59
    >>> time1.second = 0
    >>> print_time(time1)
    11:59:00
    """
    print(f"{time.hour:02d}" + ":" + f"{time.minute:02d}" + ":" + f"{time.second:02d}")
