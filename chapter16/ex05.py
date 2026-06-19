from ex01 import Time, print_time
from ex04 import time_to_int, int_to_time, is_time_valid, add_times
from copy import deepcopy


def mul_time(time: Time, n: float) -> Time:
    """Принимает объект Time и целое число и возвращает новый объект Time, который содержит произведение исходного времени и числа n.
    >>> time1 = Time()
    >>> time1.hour, time1.minute, time1.second = 11, 59, 30
    >>> print_time(mul_time(time1, 0))
    00:00:00

    >>> print_time(mul_time(time1, 2))
    23:59:00

    >>> print_time(mul_time(time1, 3))
    11:58:30

    >>> time2 = Time()
    >>> time2.hour, time2.minute, time2.second = 11, 59, -9
    >>> print_time(mul_time(time2, 3))
    Traceback (most recent call last):
    ValueError: invalid Time object in add_times
    """
    if not is_time_valid(time):
        raise ValueError("invalid Time object in add_times")
    all_time_sec = int(time_to_int(time) * n)
    return int_to_time(all_time_sec)


def average_pace(time: Time, s: float) -> Time:
    """Принимает объект Time, представляющий время окончания гонки, и число, представляющее расстояние,
    и возвращает объект Time, представляющий средний темп (часов, минут и секунд на один километр).
    >>> time1 = Time()
    >>> time1.hour, time1.minute, time1.second = 11, 59, 30
    >>> print_time(average_pace(time1, 0))
    Traceback (most recent call last):
    ValueError: s cannot be equal to zero

    >>> print_time(average_pace(time1, 2.7))
    04:26:28

    >>> time2 = Time()
    >>> time2.hour, time2.minute, time2.second = 11, 59, -9
    >>> print_time(average_pace(time2, 3))
    Traceback (most recent call last):
    ValueError: invalid Time object in add_times
    """
    if s == 0:
        raise ValueError("s cannot be equal to zero")
    return mul_time(time, 1 / s)


# Решение задачи: "Если я вышел из дома в 6:07 утра и пробежал 1 км в легком темпе
# (1 км за 8 мин. 15 сек.), потом 3 км в среднем темпе (1 км за 7 мин. 12 сек.) и 1 км
# в легком темпе снова, то во сколько я вернусь домой позавтракать?
# Результат для самопроверки: 6:45:06"

time1 = Time()
time1.hour, time1.minute, time1.second = 6, 7, 0

s1 = 1
time_s1 = Time()
time_s1.hour, time_s1.minute, time_s1.second = 0, 8, 15

s2 = 3
time_s2 = Time()
time_s2.hour, time_s2.minute, time_s2.second = 0, 7, 12
time_s2 = mul_time(time_s2, 3)

s3 = 1
time_s3 = deepcopy(time_s1)

breakfast_time = add_times(time1, time_s1, time_s2, time_s3)
print_time(breakfast_time)
# Ответ: 06:45:06
