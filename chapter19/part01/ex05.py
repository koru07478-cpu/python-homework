import pytest


def avoids(word: str, forbidden: str) -> bool:
    """Возвращает True, если в слове word нет ни одной буквы из строки forbidden."""
    return not any(letter in forbidden for letter in word)


def test_count_it():
    assert all([avoids("", ""), avoids("a", ""), avoids("", "x")])
    assert (avoids("banana", "xyz"), avoids("apple", "p"), avoids("Python", "p")) == (True, False, True)
    print("Все тесты для avoids успешно пройдены!")


if __name__ == "__main__":
    pytest.main([__file__])
