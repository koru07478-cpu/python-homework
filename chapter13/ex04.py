#Программа читает текст книги и список всех слов английского языка, а затем
#выводит все слова из книги, которых нет в этом списке.

import lib

liist_manifesto = lib.parse_words(lib.read_file("manifesto.txt"))
liist_words = lib.parse_words(lib.read_file("words13.txt"))

not_on_the_list = []
for word_manifesto in liist_manifesto:
    if word_manifesto not in liist_words:
        not_on_the_list.append(word_manifesto)

print(not_on_the_list)

#какие-то старнности при запуске, но работает
