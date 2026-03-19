# Упражнение 6.1
def compare(x: float, y: float) -> float:
    """Возвращает больше (возвртатит 1), меньше (возвратит -1) или равно (возвратит 0) первое число x относительно второго числа y"""
    if x > y:
     return 1
    if x == y:
     return 0
    else:
     return -1

print(compare(-5, 5))
