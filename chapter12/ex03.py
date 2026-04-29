with open(r'C:\Users\Alex\PycharmProjects\python-homework\chapter12\file.txt', 'r', encoding='utf-8') as f:
    words = f.read().split()
    d = {}
    for word in words:
        clean_word = word.strip('.,!?;:()[]{}<>"-').lower()
        if not clean_word.isalpha():
            continue

        key = ''.join(sorted(clean_word))

        if key not in d:
            d[key] = {word}
        else:
            d[key].add(word)

    for i in d.values():
        if len(i) > 1:
            print(list(i))

