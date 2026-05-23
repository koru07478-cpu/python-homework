import sys


def first_last(letter: str, st: str) -> tuple[int, int] | tuple[None, None]:
    """" Задача 8.2
    Требуется определить индексы первого и последнего вхождения буквы в строке.
Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, st – целевая строка.
В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть, то кортеж будет состоять из первого и последнего индекса этого символа.

    >>> first_last('a', 'abba')
    (0, 3)
    >>> first_last('a', 'abbaaaab')
    (0, 6)
    >>> first_last('a', 'a')
    (0, 0)
    >>> first_last('a', 'spring')
    (None, None)
    """

    first = st.find(letter)
    if first < 0:
        print("ветка if", file=sys.stderr)  # я просто хотел что бы он мне возращал мне одно и то же
        return None, None
    else:
        print("ветка else", file=sys.stderr)
        return first, st.rfind(letter)
