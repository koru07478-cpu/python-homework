def is_reverse(word1: str, word2: str) -> bool:
   """Проверить, являются ли word1 и word2 обращением друг друга
   >>> is_reverse('порт', 'троп')
   True
   >>> is_reverse('прив', 'кирп')
   False
   """
   if len(word1) != len(word2):
       return False
   i = 0
   j = len(word2)-1
   while j > 0:
       if word1[i] != word2[j]:
           return False
       i = i+1
       j = j-1
   return True
   
print(is_reverse("прив","кирп")) #выводит True




#ИСПРАВЛЕННЫЙ КОД (добавляю символ "=" в цикл while)
def is_reverse(word1: str, word2: str) -> bool:
   """Проверить, являются ли word1 и word2 обращением друг друга
   >>> is_reverse('порт', 'троп')
   True
   >>> is_reverse('прив', 'кирп')
   False
   """
   if len(word1) != len(word2):
       return False
   i = 0
   j = len(word2)-1
   while j >= 0:
       if word1[i] != word2[j]:
           return False
       i = i+1
       j = j-1
   return True
   
