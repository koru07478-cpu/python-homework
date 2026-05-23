def camel(st: str) -> str :
    """
    >>> camel('Утром!! было! солнечно!!!!')
    'УтРоМ!! БыЛо! СоЛнЕчНо!!!!'
    >>> camel('КРАСО4757ТА)))')
    'КрАсО4757тА)))'
    >>> camel('дождливЫЙ, вечеР??')
    'ДоЖдЛиВыЙ, вЕчЕр??'
    >>> camel('65875685!')
    '65875685!'
    """
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if letter_counter % 2 == 0:
            new_st += val.upper()
        else:
            new_st += val.lower()
        letter_counter += 1

    return new_st

