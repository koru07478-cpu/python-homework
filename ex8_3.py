from collections import Counter

def top3(st: str) -> list[tuple[str, int]]:
    """
    >>> top3('')
    []
    >>> top3('Голова думала')
    [('а', 3), ('о', 2), ('л', 2)]

    """

    freq = {}
    for char in st.lower().replace(' ', ''):
        freq[char] = freq.get(char, 0) + 1
    return Counter(freq).most_common(3)
