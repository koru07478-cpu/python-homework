def read_file(filename: str) -> list[str]:
    """Читает файл построчно в список."""
    list_result = list()
    with open(filename, 'r', encoding="utf-8-sig") as file:
        for line in file:
            list_result.append(line.strip())
    return list_result


def parse_words(lines: list[str]) -> list[str]:
    """Разбивает список строк на слова, очищает от пунктуации и переводит в нижний регистр.
    >>> parse_words(["Первая строка.", "Вторая строка."])
    ['первая', 'строка', 'вторая', 'строка']
    >>> parse_words(["Первая строка.", "", "Вторая строка."])
    ['первая', 'строка', 'вторая', 'строка']
    """
    clean_words = []
    for line in lines:
        if not line:
            continue
        for word in line.split():
            cleaned = word.strip('!"#$%&\'()*+,-./—:;“<=>?@[\\]^_`{|}~»«').lower()

            if cleaned:
                clean_words.append(cleaned)
    return clean_words
#какие-то спецсиволы все равно почему-то остаются


def histogram(words: list[str]) -> dict[str, int]:
   """Создает гистограмму слов.
   Гистограмма - словарь, сопоставляющий каждому слову из списка количество раз, которое это слово встречается в списке.
   >>> histogram(['первая', 'строка', 'вторая', 'строка'])
   {'первая': 1, 'строка': 2, 'вторая': 1}
   """
   diict = {}
   for word in words:
       if word not in diict:
           diict[word] = 1
       else:
           diict[word] += 1
   return(diict)

