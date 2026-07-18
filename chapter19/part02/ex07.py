from collections import defaultdict
import pytest


def classify_words(words: list[str]) -> dict[str, list[str]]:
    """Функция принимает список слов и возвращает словарь, в котором
    каждой букве сопоставлен список слов, которые начинаются с этой буквы."""
    d = defaultdict(list)
    for word in words:
        if word:
            d[word[0]].append(word)
    return dict(d)


def test_classify_words():
    assert classify_words(["яблоко", "банан", "ягода", "апельсин"]) == {
        "я": ["яблоко", "ягода"],
        "б": ["банан"],
        "а": ["апельсин"],
    }
    assert classify_words([""]) == {}
    assert classify_words(["кот", "", "крот"]) == {"к": ["кот", "крот"]}
    print("Все тесты для classify_words успешно пройдены!")


if __name__ == "__main__":
    pytest.main([__file__])
