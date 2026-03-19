# Упражнение 6.5

def is_power(a: int, b: int) -> bool:
  if a == b:
   return True
  if a == 1:
   return True
  if b == 1:
    return a == 1  
  if a == 0:
   return False
  if b == 0:
   return a==0
  if a%b!=0:
   return False
  return is_power(a/b, b)
 
 
print(is_power(8, 2))

#!!! гигансткая проблема этого кода в том, что он не учитывает "а" в отрицатлеьной степени, и вообще дроби едут к бесконечной рекурсии... Исправлять?
