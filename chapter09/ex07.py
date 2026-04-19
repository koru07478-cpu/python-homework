#Ответ: bookkeeper, bookkeepers, bookkeeping, bookkeepings
def has_three_pairs_identical_letters(word):
    """Проверяет, наличие в слове трех последовательных удвоенных букв"""
    for i in range(len(word) - 5):
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            return True
    return False

with open('../words.txt') as f:
    for line in f:
        word = line.strip()
        if has_three_pairs_identical_letters(word):
            print(word)
