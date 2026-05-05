import lib

def main():
    book_words = lib.parse_words(lib.read_file("manifesto.txt"))
    print(book_words)

main()

