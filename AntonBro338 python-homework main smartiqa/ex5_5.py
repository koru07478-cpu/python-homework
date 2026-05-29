from collections import Counter
from functools import reduce
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}


def sum_dct(*dicts: dict[int, int]) -> dict[int, int]:
    """"
    >>> sum_dct(dict_1, dict_4, dict_3)
    {1: 12, 2: 36, 3: 14, 4: 83, 5: 33, 6: 98, 9: 9, 10: 556, 7: 25, 8: 71}
    >>> sum_dct(dict_1, dict_2, dict_3, dict_4)
    {1: 24, 2: 36, 3: 21, 4: 84, 5: 35, 6: 98, 7: 137, 8: 71, 9: 9, 10: 556}
    >>> sum_dct()
    {}
    >>> sum_dct({1: 2}, {3: 4})
    {1: 2, 3: 4}
    """
    dict_sum_dct = {}
    for d in dicts:
        for k, v in d.items():
            dict_sum_dct[k] = dict_sum_dct.get(k, 0) + v
    return dict_sum_dct

def max_dct(*dicts: dict[int, int]) -> dict[int, int]:
    """"
    >>> max_dct(dict_1, dict_2)
    {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90, 7: 112}
    >>> max_dct(dict_1, dict_2, dict_3, dict_4)
    {1: 12, 2: 33, 3: 10, 4: 60, 5: 31, 6: 90, 7: 112, 8: 71, 9: 9, 10: 556}
    >>> max_dct()
    {}
    >>> max_dct({1: 2}, {2: 10})
    {1: 2, 2: 10}
    >>> max_dct({1: 2}, {1: 10})
    {1: 10}
    """
    dict_max_dct = {}
    for d in dicts:
        for k, v in d.items():
            if v > dict_max_dct.get(k, float('-inf')):
                dict_max_dct[k] = v
    return dict_max_dct


