

def biggest_dict(**kwargs) -> dict[str, str | int]:
    """"
    >>> biggest_dict(k1=22, k2=31, k3=11, k4=91)
    {'k1': 22, 'k2': 31, 'k3': 11, 'k4': 91}
    >>> biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
    {'name': 'Елена', 'age': 31, 'weight': 61, 'eyes_color': 'grey'}
    """
    my_dict = {}
    my_dict.update(**kwargs)
    return my_dict

