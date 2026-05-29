from collections import Counter

def top3(st: str) -> list[tuple[str, int]]:
    """
    >>> top3('')
    []
    >>> top3('Голова думала')
    [('а', 3), ('о', 2), ('л', 2)]
    """
    counter = Counter(st.lower().replace(' ', ''))
    return counter.most_common(3)