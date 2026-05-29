def search_substr(subst: str, st: str) -> str:
    """
    >>> search_substr('w', 'warriors')
    'Есть контакт!'
    >>> search_substr('WOR', 'work')
    'Есть контакт!'
    >>> search_substr('word', 'work')
    'Мимо!'
    """
    return 'Есть контакт!' if subst.lower() in st.lower() else 'Мимо!'