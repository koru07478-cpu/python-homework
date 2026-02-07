
def do_twice(function):
   function()
   function()

def print_spam():
	def print_spam_once():
		print('спам')
		
	do_twice(print_spam_once)


def do_four(function, argument):
   function(argument)
   function(argument)
   function(argument)
   function(argument)

def do_four_short(function, argument):
	"""Предыдущая проще в понимании чем эта, тк тут есть рекурсия. Но лучше эта, тк она компактней с одной стороны (но и хуже тем, что рекурсия без мемоизации)"""
	def function_once():
	    function(argument)  
		
	do_twice(function_once)
	do_twice(function_once)
	
	
#Проверка:

print_spam()
print(do_four(print, "cat"))
print(do_four_short(print, "dog"))
