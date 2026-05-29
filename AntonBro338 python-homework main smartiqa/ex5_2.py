def biggest_dict(**kwargs) -> dict[str, str | int]:
    """
    >>> biggest_dict(k1=22, k2=31, k3=11, k4=91)
    {'first_one': 'we can do it', 'k1': 22, 'k2': 31, 'k3': 11, 'k4': 91}
    >>> biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
    {'first_one': 'we can do it', 'name': 'Елена', 'age': 31, 'weight': 61, 'eyes_color': 'grey'}
    >>> biggest_dict()
    {'first_one': 'we can do it'}
    """
    return {"first_one": "we can do it", **kwargs}
