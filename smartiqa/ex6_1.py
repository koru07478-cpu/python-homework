from typing import Any

def tpl_sort(tpl: tuple[Any, ...]) -> tuple[Any, ...]:
    """
    Cортирует кортеж, чтобы он состоял из целых чисел по возрастанию, и возвращает его. Если хотя бы
    один элемент не является целым числом, то функция возвращает исходный кортеж.
    >>> tpl_sort((6, 3, 5, 2, 1))
    (1, 2, 3, 5, 6)
    >>> tpl_sort((6, 1, 4.0, 7))
    (6, 1, 4.0, 7)
    >>> tpl_sort((6, 1, 4.7, 7))
    (6, 1, 4.7, 7)
    >>> tpl_sort((6, 1, 4, 7))
    (1, 4, 6, 7)
    >>> tpl_sort((5, 5, 2.1, '1', 9))
    (5, 5, 2.1, '1', 9)
    >>> tpl_sort(tuple())
    ()
    """
    for i in tpl:
        if type(i) is not int:
            return tpl
    return tuple(sorted(tpl))