def tpl_sort(t) -> float:
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
    >>> tpl_sort(())
    ()
    >>> tpl_sort((2, 'abc', 1))
    (2, 'abc', 1)
    """
    liist = []
    for i in t:
        if isinstance(i, int):
            liist.append(i)
        elif isinstance(i, float):
            return t
    return tuple(sorted(liist))