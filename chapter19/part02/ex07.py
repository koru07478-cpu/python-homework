from collections import defaultdict


def classify_words(words: list[str]) -> dict[str, list[str]]:
    """Функция принимает список слов и возвращает словарь, в котором
    каждой букве сопоставлен список слов, которые начинаются с этой буквы.
    >>> classify_words(['яблоко', 'банан', 'ягода', 'апельсин'])
    {'я': ['яблоко', 'ягода'], 'б': ['банан'], 'а': ['апельсин']}
    >>> classify_words([])
    {}
    >>> classify_words(['кот', '', 'крот'])
    {'к': ['кот', 'крот']}
    """
    d = defaultdict(list)
    for word in words:
        if word:
            d[word[0]].append(word)
    return dict(d)
