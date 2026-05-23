def cleaned_str(st: str) -> str :
    """"
    >>> cleaned_str('Гр@оо@лк@оц@ва')
    'Голова'
    >>> cleaned_str('сварка@@@@@лоб@ну@')
    'слон'
    """
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)

