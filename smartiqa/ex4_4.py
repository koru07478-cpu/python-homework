def useless(lst: list[int | float | str]) -> float  | None:
    """
    Берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка.
    >>> useless([0, "cat"])
    0.0
    >>> useless([0, 1.1, "cat", "Dog", -1])
    0.3666666666666667
    >>> useless([])

    """
    liist = []
    for i in lst:
        if isinstance(i, (int, float)):
            liist.append(i)

    if not liist:
        return None

    return max(liist) / len(liist)