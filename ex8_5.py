def shortener(st: str) -> str:
    """"
    >>> shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)')
    'Падал прошлогодний снег'
    >>> shortener('(лишнее(лишнее))Падал прошлогодний (лишнее(лишнее(лишнее)))снег')
    'Падал прошлогодний снег'
    """
    finish_text = []
    depth_text = 0
    for char in st:
        if char == '(':
            depth_text += 1
        elif char == ')':
            if depth_text > 0:
                depth_text -= 1
        elif depth_text == 0:
            finish_text.append(char)
    return ' '.join(''.join(finish_text).split())

