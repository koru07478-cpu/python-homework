def has_digit(s: str) -> bool:
    """Возвращает True, когда в строке есть хотя бы одна цифра '0'…'9'.
    >>> has_digit("abc1def")
    True
    >>> has_digit("text")
    False
    >>> has_digit("123")
    True
    >>> has_digit("")
    False
    """
    return any(i in "0123456789" for i in s)
