with open(r'../words.txt', 'r', encoding='utf-8') as f:
    words = f.read().split()
    # файл прочитали, можно закрыть

d = {}
for word in words:
    clean_word = word.strip('.,!?;:()[]{}<>"-').lower()
    if not clean_word.isalpha():
        continue

    key = ''.join(sorted(clean_word))

    if key not in d:  # setdefault подошёл бы идеально
        d[key] = {word}  # множества?
    else:
        d[key].add(word)

for i in d.values():
    if len(i) > 1:
        print(list(i))

# и в конце нужно отсортировать по количеству анаграмм