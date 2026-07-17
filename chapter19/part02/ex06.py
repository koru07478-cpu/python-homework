from collections import Counter
import pytest


def count_it(sequence: str) -> dict[int, int]:
    """Функция принимает строку, содержащую последовательность чисел от 0 до 9, создает и возвращает словарь
    с тремя наиболее часто встречающимися числами, который в качестве ключей будет принимать данные числа (т. е.
    ключи будут типом int), а в качестве значений — количество этих чисел в имеющейся последовательности."""
    return {int(key): value for key, value in Counter(sequence).most_common(3)}


def test_count_it():
    assert count_it("999998888777665") == {9: 5, 8: 4, 7: 3}
    assert count_it("55") == {5: 2}
    assert count_it("") == {}
    print("Все тесты для count_it успешно пройдены!")


if __name__ == "__main__":
    pytest.main([__file__])
