from ex01 import Time, print_time
from copy import deepcopy


def incremented_time(time: Time, seconds: int) -> Time:
    """«Чистая» функция, которая добавляет указанное количество секунд к объекту Time, не используя циклы.
    (Создает и возвращает новый объект Time, а не изменяет параметр.)
    >>> time1 = Time()
    >>> time1.hour, time1.minute, time1.second = 22, 59, 30
    >>> print_time(incremented_time(time1, 100))
    23:01:10

    >>> print_time(incremented_time(time1, 3700))
    00:01:10

    >>> # Проверка на "чистоту":
    >>> _ = incremented_time(time1, 500)
    >>> print_time(time1)
    22:59:30
    """
    result = deepcopy(time)
    result.second += seconds
    if result.second >= 60:
        result.minute += result.second // 60
        result.second %= 60
    if result.minute >= 60:
        result.hour += result.minute // 60
        result.minute %= 60
    result.hour %= 24

    return result
