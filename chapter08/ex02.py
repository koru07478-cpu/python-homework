def find(string: str, ministring: str) -> int:
   """Возвращает индекс вхождения министроки `ministring` в строку `string`.


   Возвращает -1, если такого вхождения нет.


   >>> find('abc', 'b')
   1
   >>> find('alphabetagamma', 'beta')
   5
   >>> find('abc', 'd')
   -1
   """
   index = 0
   while index < len(string):
       if string[index:(index+len(ministring))] == ministring:
           return index
       index = index + 1
   return -1

print(find("homak", "mak"))
