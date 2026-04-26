def histogram(string: str) -> dict[str, int]:
   """
   Считает количество каждого символа в строке string возвращает dict[str, int], где string - тип ключа, а integer - это тип значения.

   >>> histogram("HeLLoo, Паша")
   {'H': 1, 'e': 1, 'L': 2, 'o': 2, ',': 1, ' ': 1, 'П': 1, 'а': 2, 'ш': 1}
   >>> histogram(")*&&@*!#$$%")
   {')': 1, '*': 2, '&': 2, '@': 1, '!': 1, '#': 1, '$': 2, '%': 1}
   >>> histogram("9000888")
   {'9': 1, '0': 3, '8': 3}
   >>> histogram("")
   {}
   """
   hist = dict()
   for char in string:
        hist[char] = hist.get(char, 0) + 1
   return hist

print(histogram("helloo"))
