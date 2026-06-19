from ex01 import Time, print_time


def time_to_int(time: Time) -> int:
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds: int) -> Time:
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    hour, time.minute = divmod(minutes, 60)
    day, time.hour = divmod(hour, 24)
    return time


def is_time_valid(time: Time) -> bool:
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60 or time.hour >= 24:
        return False
    return True


def add_times(*ti: Time) -> Time:
    """«Чистая» функция, которая складывает произовльное количество времени типа Time.
    >>> print_time(add_times())
    00:00:00

    >>> time1 = Time()
    >>> time1.hour, time1.minute, time1.second = 11, 59, 30
    >>> time2 = Time()
    >>> time2.hour, time2.minute, time2.second = 11, 59, 11
    >>> time3 = Time()
    >>> time3.hour, time3.minute, time3.second = 0, 0, 0
    >>> time4 = Time()
    >>> time4.hour, time4.minute, time4.second = 11, 59, 11

    >>> print_time(add_times(time1))
    11:59:30

    >>> # Проверка на "чистоту":
    >>> _ = add_times(time1, time2)
    >>> print_time(time1)
    11:59:30
    >>> print_time(time2)
    11:59:11

    >>> print_time(add_times(time1, time2, time3, time4))
    11:57:52

    >>> time5 = Time()
    >>> time5.hour, time5.minute, time5.second = 11, 81, 30
    >>> print_time(add_times(time1, time2, time3, time4, time5))
    Traceback (most recent call last):
    ValueError: invalid Time object in add_times
    """
    seconds = 0
    for i in ti:
        if not is_time_valid(i):
            raise ValueError("invalid Time object in add_times")
        seconds += time_to_int(i)
    return int_to_time(seconds)
