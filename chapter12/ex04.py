with open('../words.txt', 'r', encoding='utf-8') as f:
    words = set(word.strip('.,!?;:()[]{}<>"-').lower() for word in f.read().split())
    words = [w for w in words if w.isalpha()]

d = {}
for word in words:
    key = ''.join(sorted(word))
    d.setdefault(key, []).append(word)   # setdefault (галочка)

for similar_words in d.values():  # i очень долго живёт, стоит переименовать (галочка)
    if len(similar_words) < 2:
        continue

    for i, fer in enumerate(similar_words):
        for sec in similar_words[i + 1:]:
            if len(fer) != len(sec):
                continue
            # можно было сделать enumerate в цикле выше (галочка)
            # а тут индекс в принципе дальше не нужен, можно было сразу букву перебирать по срезу (галочка)

            liist = []

            for m, (a, b) in enumerate(zip(fer, sec)):
                if a != b:
                    liist.append(m) # а тут можно было через zip (галочка)

            if len(liist) == 2:
                print(f"{fer} - {sec}")

#спасибо за комментарии!
