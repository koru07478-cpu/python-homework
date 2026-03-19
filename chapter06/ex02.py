# Упражнение 6.2
def fibonacci(n: int, depth: int = 0) -> int:
    """Возвращает n-ное число в последовательности Фибоначчи"""
    indent = ' | ' * depth
    
    assert isinstance(n, int), 'Фибоначчи определяется только для целых чисел.'
    assert n >= 0, 'Фибоначчи не определяется для отрицательных целых чисел.'
    print(indent, 'fibonacci(', n, ')')
    
    if n == 0:
        print(indent, 'возвращает 0 (базовое условие)')
        return 0
    if n == 1:
        print(indent, 'возвращает 1 (базовое условие)')
        return 1
    
    deeper = depth + 1
    result = fibonacci(n - 1, depth=deeper) + fibonacci(n - 2, depth=deeper)
    
    print(indent, 'возвращает', result)
    return result
    


print("fibonacci(5) = ", fibonacci(5))
