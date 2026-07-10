def dict_zip(keys: list, values: list) -> dict:
    """Принимает два списка одинаковой длины и возвращает словарь, в котором ключи и значения
    сопоставлены друг с другом в том же порядке, в каком они представлены в списках.
    >>> dict_zip(["cat1", "cat2", "cat3"], ["Tom", "Bob", "Max"])
    {'cat1': 'Tom', 'cat2': 'Bob', 'cat3': 'Max'}
    >>> dict_zip([], [])
    {}
    >>> dict_zip(["a", "b", "a"], [1, 2, 3])
    {'a': 3, 'b': 2}
    """
    return {key: value for key, value in zip(keys, values)}
