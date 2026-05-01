with open(r'../words.txt', 'r', encoding='utf-8') as f:
    words = f.read().split()

d = {}
for word in words:
    clean_word = word.strip('.,!?;:()[]{}<>"-').lower()
    if not clean_word.isalpha():
        continue

    key = ''.join(sorted(clean_word))
    d.setdefault(key, set()).add(word)

seq = []
for i in d.values():
    if len(i) > 1:
        seq.append(list(i))

# и в конце нужно отсортировать по количеству анаграмм (галочка)
seq.sort(key=len, reverse=True)

for g in seq:
    print(g)
