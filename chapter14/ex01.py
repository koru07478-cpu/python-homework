def replace_lines(pattern: str, replacement: str, input_file: str, output_file: str) -> None:
    """
    Функция считывает содержимое `input_file` и копирует его в `output_file` (создавая его при необходимости).
    Если `pattern` встречается где-либо в `input_file`, её следует заменить на `replacement`.
    В случае исключения функция печатает сообщение об ошибке и завершает работу.

    :param pattern: Шаблон для поиска в файле.
    :param replacement: Строка, на которую нужно заменять шаблон.
    :param input_file: Имя входного файла.
    :param output_file: Имя выходного файла
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file_in:
            with open(output_file, 'w', encoding='utf-8') as file_ou:
                for line in file_in:
                    new_line = line.replace(pattern, replacement)
                    file_ou.write(new_line)


    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")

    except PermissionError:
        print(f"Ошибка: Нет доступа к файлу '{input_file}' или '{output_file}'.")

    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")

    except Exception as ex:
        print(f"Что-то пошло не так: {ex}")


def main():
    replace_lines("p", "r", "input.txt", "output.txt")


if __name__ == "__main__":
    main()
