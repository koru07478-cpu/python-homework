from typing import Iterator


def sum_five(it: Iterator[int]) -> int:
    """Функция складывает первые 5 элементов последовательности
    >>> sum_five([1, 2, 3, 4]) #(Код ждет итератор)
    10
    >>> sum_five([1, 2, 3, 4, 5, 1000]) #(Код ждет итератор)
    15
    >>> sum_five((x*x for x in range(1, 1000000000)))
    55
    >>> sum_five([x*x for x in range(1, 1000000000)])
    >>> #Код выполняется* капец долго, тк в начале заполняет список. А вот в случае
    >>> #с выражением-генератором каждое значение итератора сразу идет в ход.
    >>> #*Я самого выполенния доктеста так и не дождалась.
    55
    """
    total = 0
    for index, item in enumerate(it):
        total += item
        if index == 4:
            break
    return total
