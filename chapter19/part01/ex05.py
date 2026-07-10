def avoids(word: str, forbidden: str) -> bool:
    """Возвращает True, если в слове word нет ни одной буквы из строки forbidden.
    >>> all([avoids("", ""), avoids("a", ""), avoids("", "x")])
    True
    >>> avoids("banana", "xyz"), avoids("apple", "p"), avoids("Python", "p")
    (True, False, True)
    """
    return not any({letter in forbidden for letter in word})
