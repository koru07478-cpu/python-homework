def has_duplicates(t: list) -> bool:
    """
    Принимает словарь и возвращает True, если есть какое-либо значение, 
    которое появляется более одного раза. Она не изменяет исходный словарь
    >>> has_duplicates([1, 2, 1])
    True
    >>> has_duplicates([1, 2, 3])
    False
    >>> has_duplicates([])
    False
    """
    hist = dict()
    for val in t:
        hist[val] = hist.get(val, 0) + 1
        if hist[val] > 1:
            return True
    return False
