def any_lowercase1(s: str) -> bool:
   """ Проверяет первый сивол на нижний регистр. 
   >>> any_lowercase1('FrOG')
   False
   """
   for c in s:
       if c.islower():
           return True
       else:
           return False




def any_lowercase2(s: str) -> str:
   """ Проверяет символ 'с' на нижний регистр. Всегда вернет 'True'.
   >>> any_lowercase2('FROG')
   'True'
   """
   for c in s:
       if 'c'.islower():
           return 'True'
       else:
           return 'False'




def any_lowercase3(s: str) -> bool:
   """ Проверяет последний сивол на нижний регистр.
   >>> any_lowercase3('froG')
   False
   """
   for c in s:
       flag = c.islower()
   return flag




def any_lowercase4(s: str) -> bool:
   """ Проверяет на наличие хотя бы одного сивола в нижнем регистре. 
   >>> any_lowercase4('FrOG')
   True
   """
   flag = False
   for c in s:
       flag = flag or c.islower()
   return flag




def any_lowercase5(s: str) -> bool:
   """ Проверяет на отсутствие всех сивмолов, кроме сиволов в нижнем регистре.
   >>> any_lowercase5('frOg')
   False
   """
   for c in s:
       if not c.islower():
           return False
   return True
