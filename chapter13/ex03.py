import lib

#N1. Общее количество слов в книге.
print(len(lib.parse_words(lib.read_file("manifesto.txt"))))

#N2. Количество разных слов, использованных в книге.
liist = lib.parse_words(lib.read_file("manifesto.txt"))
liist_no_repetitions = []
for word in liist:
    if word not in liist_no_repetitions:
        liist_no_repetitions.append(word)
print(len(liist_no_repetitions))

#N3. Двадцать наиболее часто используемых в книге слов и количество каждого из них.
from operator import itemgetter

words = lib.parse_words(" ".join(lib.parse_words(lib.read_file("manifesto.txt"))).split())
h = lib.histogram(words)
top_20_list = sorted(h.items(), key=itemgetter(1), reverse=True)[:20]
print(top_20_list)


