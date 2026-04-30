with open('../chapter12/words.txt') as f:
    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word)
