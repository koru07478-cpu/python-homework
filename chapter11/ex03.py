def histogram(string: str) -> dict[str, int]:
   """
   Считает количество каждого символа в строке string возвращает dict[str, int], где string - тип ключа, а integer - это тип значения.
   """
   hist = dict()
   for char in string:
        hist[char] = hist.get(char, 0) + 1
   return hist

def invert_dict1(d: dict[K, V]) -> dict[V, list[K]]:
   """
      Инвертирует словаврь, меняя значенияч на ключи, а ключи на значения.
      На каждой итерации цикла переменная key получает ключ из словаря d,
   а value получает соответствующее значение. Если значения value нет в inverse,
   это означает, что мы не встречали его раньше, поэтому мы создаем новый элемент
   и инициализируем его с помощью одноэлементного списка.
   >>> invert_dict1({})
   {}
   >>> invert_dict1({'dog': 1, 'pig': 1, 'cat': 2})
   {1: ['dog', 'pig'], 2: ['cat']}
   >>> invert_dict1({1/9: 1, 1.0: 1, 1+0: 2})
   {1: [0.1111111111111111], 2: [1.0]}
   """
   inverse = dict()
   for key in d:
       value = d[key]
       if value not in inverse:
           inverse[value] = [key]
       else:
           inverse[value].append(key)
   return inverse

def invert_dict2(d: dict[K, V]) -> dict[V, list[K]]:
    """
    Инвертирует словаврь, меняя значенияч на ключи, а ключи на значения.
    >>> invert_dict1({})
    {}
    >>> invert_dict1({'dog': 1, 'pig': 1, 'cat': 2})
    {1: ['dog', 'pig'], 2: ['cat']}
    >>> invert_dict1({1/9: 1, 1.0: 1, 1+0: 2})
    {1: [0.1111111111111111], 2: [1.0]}
    """
    inverse = dict()
    for key in d:
        inverse.setdefault("key", 0)
    return inverse
