#a – это число, из которого мы извлекаем квадратный корень

import math

def mysqrt(a):
    x = a / 2  
    epsilon = 0.0000001
    
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y  
        x = y

def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    
    for a in range(1, 10):
        print(str(a) + " " + str(mysqrt(a)) + " " + str(math.sqrt(a)) + " " + str(abs(mysqrt(a) - math.sqrt(a))))

test_square_root()
