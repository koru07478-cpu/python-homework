def print_most_frequent(s: str):
    """ Принимает строку, и печатает буквы в порядке убывания их частотности в этой строке.
    >>> print_most_frequent("Привет, 49")
    т р и е в П
    """
    d = dict()
    for i in s:
        if i.isalpha():  # Убирает цифры, пробелы и знаки препинания
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    liist = []
    for key, value in d.items():
        liist.append((value, key))
    liist.sort(reverse=True)
    for j in liist:
        print(j[1], end=' ')
