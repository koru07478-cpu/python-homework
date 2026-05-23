def to_dict(lst: list) -> dict:
    """
    >>> to_dict([1, 2, 3, 4])
    {1: 1, 2: 2, 3: 3, 4: 4}
    >>> to_dict(['grey', (2, 17), 3.11, -4])
    {'grey': 'grey', (2, 17): (2, 17), 3.11: 3.11, -4: -4}
    """
    dict_elements = {}
    for element in lst:
        dict_elements[element] = element
    return dict_elements
