

from collections import Counter

def count_it(sequence: str) -> dict:
    """"
    >>> count_it('1111111111222')
    {'1': 10, '2': 3}
    >>> count_it('123456789012133288776655353535353441111')
    {'3': 8, '1': 7, '5': 7}
    >>> count_it('007767757744331166554444')
    {'7': 6, '4': 6, '6': 3}
    """
    return dict(Counter(sequence).most_common(3))

