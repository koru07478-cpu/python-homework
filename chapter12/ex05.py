# Список слов в файле words.txt не содержит однобуквенных слов.
# Поэтому  в качестве базового случая мы можем взять слова “i” и “a”.
words = set()
with open('words.txt', 'r') as f:
    for line in f:
        words.add(line.strip().lower())
words.update(['a', 'i', ''])


def a_letter_equals_a_new_word(word):
    """
    Рекурсивно ищет цепочку сокращений слова до одной буквы.
    Возвращает список слов или [], если сокращение невозможно.
    >>> a_letter_equals_a_new_word("split")
    ['split', 'slit', 'lit', 'it', 'i']
    """
    if word not in words:
        return []
    if len(word) <= 1:
        return [word]

    for i in range(len(word)):
        res = a_letter_equals_a_new_word(word[:i] + word[i + 1:])
        if res:
            return [word] + res
    return []


all_words = sorted(list(words), key=len, reverse=True)

for w in all_words:
    seq = a_letter_equals_a_new_word(w)
    if seq:
        print(f"{w} -> {seq}")
        break
