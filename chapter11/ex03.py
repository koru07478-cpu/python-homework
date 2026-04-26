def histogram(string: str) -> dict[str, int]:
    """
    Считает количество каждого символа в строке string возвращает dict[str, int], где string - тип ключа, а integer - это тип значения.
    """
    hist = dict()
    for char in string:
        hist[char] = hist.get(char, 0) + 1
    return hist


def invert_dict2(d: dict) -> dict:
    """
    Инвертирует словаврь, меняя значенияч на ключи, а ключи на значения.
    >>> invert_dict2({})
    {}
    >>> invert_dict2({'dog': 1, 'pig': 1, 'cat': 2})
    {1: ['dog', 'pig'], 2: ['cat']}
    >>> invert_dict2({1/9: 1, 1.0: 1, 8: 2})
    {1: [0.1111111111111111, 1.0], 2: [8]}
    """
    inverse = dict()
    for key in d:
        value = d[key]
        inverse.setdefault(value, []).append(key)
    return inverse
