import io
import random


class MarkovChain:
    def __init__(self):
        # Соответствие префиксов суффиксам:
        self.suffix_map: dict[tuple[str, ...], list[str]] = {}
        # Текущий префикс:
        self.prefix: tuple[str, ...] = ()

    def process_file(self, filename: str, order: int = 2):
        """Прочитать файл и собрать статистику.
        :param filename: имя файла
        :param order: количество слов в префиксе
        """
        with open(filename) as fp:
            skip_gutenberg_header(fp)
            for line in fp:
                if line.startswith("*** END OF THE"):
                    break
                for word in line.rstrip().split():
                    self.process_word(word.lower(), order)

    def process_word(self, word: str, order: int = 2):
        """Обработать слово
        На первых нескольких итерациях мы накапливаем prefix, потом начинаем добавлять соответствия префиксов в словарь
        """
        if len(self.prefix) < order:
            self.prefix += (word,)
            return
        self.suffix_map.setdefault(self.prefix, []).append(word)
        self.prefix = shift(self.prefix, word)

    def random_text(self, n: int = 100):
        """Сгенерировать `n` случайных слов после случайного префикса
        :param n: Количество слов для генерации после префикса
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes is None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n - i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=" ")
            start = shift(start, word)


def skip_gutenberg_header(fp: io.TextIOBase):
    """Прочитать из fp до маркера начала текста книги"""
    for line in fp:
        if line.startswith("*** START OF THE"):
            break


def shift(t: tuple[str, ...], word: str):
    """Построить новый префикс на основе предыдущего"""
    return t[1:] + (word,)


def main(filename: str = "manifesto.txt", n: int = 100, order: int = 2):
    markov_chain = MarkovChain()
    markov_chain.process_file(filename, order)
    markov_chain.random_text(n)


if __name__ == "__main__":
    main()
