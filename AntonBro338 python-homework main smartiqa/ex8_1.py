def search_substr(subst: str, st: str) -> str:
    """"
    >>> search_substr ('w', 'warriors')
    'Есть контакт!'
    >>> search_substr ('wor', 'work')
    'Есть контакт!'
    >>> search_substr ('word', 'work')
    'Мимо!'
    """
    lower_subst = subst.upper()
    lower_st = st.upper()
    if lower_subst in lower_st:
        return 'Есть контакт!'
    else:
        return 'Мимо!'