import lib


def remove_metadata(lines: list[str]) -> list[str]:
    """
    Читает загруженную книгу, но пропускает метаданные в начале файла (до строки *** START OF THE PROJECT… включительно)
    и в конце файла (от строки *** END OF THE PROJECT… включительно), а потом считывает содержимое файла, разбивает
    каждую строку на слова, удаляя пробелы и знаки препинания из слов и преобразуя их в строчные.
    """
    header_end = '*** START OF THE PROJECT GUTENBERG EBOOK THE COMMUNIST MANIFESTO ***'
    footer_start = '*** END OF THE PROJECT GUTENBERG EBOOK THE COMMUNIST MANIFESTO ***'

    list_del_metadata = []
    flag = False

    for line in lines:
        if line.startswith(header_end):
            flag = True
            continue

        if line.startswith(footer_start):
            break

        if flag:
            list_del_metadata.append(line)

    return list_del_metadata


def main():
    raw_data = lib.read_file("manifesto.txt")
    if isinstance(raw_data, str):
        raw_lines = raw_data.splitlines()
    else:
        raw_lines = raw_data
    clean_lines = remove_metadata(raw_lines)
    book_words = []

    for line in clean_lines:
        for word in line.split():
            clean_word = word.strip().lower()
            if clean_word:
                book_words.append(clean_word)

    print(book_words)


if __name__ == "__main__":
    main()


