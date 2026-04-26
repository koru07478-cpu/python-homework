def has_duplicates(t: dict) -> bool:
    """
    Принимает словарь и возвращает True, если есть какое-либо значение, 
    которое появляется более одного раза. Она не изменяет исходный словарь
    >>> has_duplicates({'dog': 1, 'pig': 1, 'cat': 2})
    True
    >>> has_duplicates({'dog': 1, 'pig': 2, 'cat': 3})
    False
    """
    hist = dict()
    for val in t.values():
        hist[val] = hist.get(val, 0) + 1
        if hist[val] > 1:
            return True
    return False
