def line_in_reverse_order(string):
    """ Принимает строку в качестве аргумента и отображает буквы в обратном порядке, по одной на строку, с помощью цикла while. """
    index = 1
    while index <= len(string):
    	letter = string[-index]
    	print(letter)
    	index = index + 1
    return "The end of string"
    	 	

print(line_in_reverse_order("aple"))
