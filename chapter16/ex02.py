from ex01 import Time, print_time


def is_after(t1: Time, t2: Time) -> bool:
    """Возвращает True, если t1 хронологически следует за t2, и False в противном случае.
    >>> # t1 > t2
    >>> time1 = Time()
    >>> time1.hour, time1.minute, time1.second = 11, 59, 30
    >>> time2 = Time()
    >>> time2.hour, time2.minute, time2.second = 11, 59, 11
    >>> is_after(time1, time2)
    True

    >>> # t1 < t2
    >>> time3 = Time()
    >>> time3.hour, time3.minute, time3.second = 0, 0, 0
    >>> is_after(time3, time2)
    False

    >>> # t1 == t2
    >>> time4 = Time()
    >>> time4.hour, time4.minute, time4.second = 11, 59, 11
    >>> is_after(time4, time2)
    False
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
