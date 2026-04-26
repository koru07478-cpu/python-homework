import time
import bisect

def create_dict():
    di = {}
    with open("words.txt", "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            di[word] = None
    return di

di = create_dict()
words_list = sorted(di.keys())
st = "banana"

# 1. Поиск в словаре (на втором месте)
start = time.perf_counter()
found_dict = st in di
t_dict = time.perf_counter() - start

# 2. Бинарный поиск в списке (самый быстрый)
start = time.perf_counter()
i = bisect.bisect_left(words_list, st)
found_bin = i < len(words_list) and words_list[i] == st
t_binaryList = time.perf_counter() - start

# 3. Оператор 'in' в списке (на третьем месте)
start = time.perf_counter()
found_list = st in words_list
t_list = time.perf_counter() - start


print(f"Результаты поиска для '{st}':")
print(f"Словарь:             {t_dict:.10f} сек")
print(f"СписокБинарный:      {t_binaryList:.10f} сек")
print(f"СписокIn :           {t_list:.10f} сек")
