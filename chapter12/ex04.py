with open('../words.txt', 'r', encoding='utf-8') as f:
    words = set(word.strip('.,!?;:()[]{}<>"-').lower() for word in f.read().split())
    words = [w for w in words if w.isalpha()]

d = {}
for word in words:
    key = ''.join(sorted(word))
    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)

for i in d.values():
    if len(i) < 2:
        continue

    for j in range(len(i)):
        for k in range(j + 1, len(i)):
            fer = i[j]
            sec = i[k]

            if len(fer) != len(sec):
                continue

            liist = []
            for m in range(len(fer)):
                if fer[m] != sec[m]:
                    liist.append(m)

            if len(liist) == 2:
                print(f"{fer} - {sec}")
