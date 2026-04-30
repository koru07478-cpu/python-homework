# Условие: Дана строка из уникальных символов. Нужно вернуть список всех возможных комбинаций этих символов.
# Пример: "abc" ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
def combined_symbols(t):
    """
    >>> combined_symbols('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    if len(t) <= 1: return [t]
    res = []
    for i in range(len(t)):
        for j in combined_symbols(t[:i] + t[i + 1:]):
            res.append(t[i] + j)
    return res

print(combined_symbols("abcd"))


