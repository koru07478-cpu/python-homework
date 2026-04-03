def count(string: str, ministring: str) -> int:
   """Возвращает количество вхождений министроки `ministring` в строку `string`.

   >>> find('babbcb', 'b')
   4
   >>> find('банан', 'а')
   2
   >>> find('abc', 'd')
   -1
   """
   index = 0
   count = 0
   while index < len(string):
       if string[index:(index+len(ministring))] == ministring:
           count += 1
       index = index + 1
   return count 

print(count("homakmak", "mak"))
