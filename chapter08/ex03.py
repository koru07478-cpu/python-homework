def count(string: str, ministring: str) -> int:
   """Возвращает количество вхождений министроки `ministring` в строку `string`.

   >>> count('babbcb', 'b')
   4
   >>> count('банан', 'а')
   2
   >>> count('банан', 'ан')
   2
   >>> count('abc', 'd')
   0
   """
   index = 0
   count = 0
   while index < len(string):
       if string[index:(index+len(ministring))] == ministring:
           count += 1
       index = index + 1
   return count 

print(count("homakmak", "mak"))
