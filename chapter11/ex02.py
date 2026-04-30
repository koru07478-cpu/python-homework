import time
import bisect
import random

def create_dict():
    di = {}
    with open("../chapter12/words.txt", "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            di[word] = None
    return di

di = create_dict()
words_list = sorted(di.keys())

# 20 случайных слов из списка
random_words = random.sample(words_list, 20)
N = 1000

total_dict = 0
total_binary = 0
total_in_list = 0

for st in random_words:
    # 1. Поиск в словаре
    t_dict = 0
    for _ in range(N):
        start = time.perf_counter()
        found_dict = st in di
        t_dict += time.perf_counter() - start
    total_dict += t_dict / N

    # 2. Бинарный поиск в списке
    t_binary_list = 0
    for _ in range(N):
        start = time.perf_counter()
        i = bisect.bisect_left(words_list, st)
        found_bin = i < len(words_list) and words_list[i] == st
        t_binary_list += time.perf_counter() - start
    total_binary += t_binary_list / N

    # 3. Оператор 'in' в списке
    t_list = 0
    for _ in range(N):
        start = time.perf_counter()
        found_list = st in words_list
        t_list += time.perf_counter() - start
    total_in_list += t_list / N

num_words = len(random_words)
print(f"Средние результаты для {num_words} случайных слов:")
print(f"Словарь:         {total_dict/num_words:.10f} сек")
print(f"Список Бинарный: {total_binary/num_words:.10f} сек")
print(f"Список 'in':     {total_in_list/num_words:.10f} сек")
