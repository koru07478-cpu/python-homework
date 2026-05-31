from typing import Any

def change(lst: list[Any]) -> list[Any]:
    """
    Принимает список и меняет местами его первый и последний элемент. В исходном списке минимум 2 элемента.
    >>> change([0, "cat"])
    ['cat', 0]
    >>> change([0, 1.1, "cat", "Dog", -1])
    [-1, 1.1, 'cat', 'Dog', 0]
    """
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

