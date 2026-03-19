# Упражнение 6.4
# 1. Во всех случаях функция middle() выведет пустую строчку.

# 2.
def first(word: str) -> str:
   """Возвращает первый символ строки"""
   return word[0]
   
def last(word: str) -> str:
   """Возвращает последний символ строки"""
   return word[-1]
   
def middle(word: str) -> str:
   """Возвращает строку без первой и последней буквы"""
   return word[1:-1]



def is_palindrome(word):
 if word == "":
  return True
 if first(word) != last(word):
  return False
 return is_palindrome(middle(word))
   

      
print(is_palindrome("рррр"))
