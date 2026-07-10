def compare(x: float, y: float) -> int:
    """Возвращает 1, если x > y, 0, если x == y, и –1, если x < y.
    >>> compare(9, -1)
    1
    >>> compare(-1, -1)
    0
    >>> compare(-9, -1)
    -1
    """
    return 1 if x > y else 0 if x == y else -1
