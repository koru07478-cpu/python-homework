import lib
import random

def choose_from_hist(hist):
    """
    Функция принимает гистограмму типа dict[str, int], и возвращает случайное значение
    из гистограммы, вероятность выбора которого пропорциональна частотности.
    """
    hist_in_list = []
    for word, count in hist.items():
        hist_in_list.extend([word] * count)
    return random.choice(hist_in_list)



print(choose_from_hist(lib.histogram(['а', 'а', 'б'])))
print(choose_from_hist(lib.histogram([1, 2, 3])))