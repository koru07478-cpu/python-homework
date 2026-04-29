def sumall(*args: int) -> int:
    """
    Принимает любое количество аргументов и возвращает их сумму.
    >>> sumall(6, 8.9, 0, -1)
    13.9
    >>> sumall()
    0
    """
    return sum(args)