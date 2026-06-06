# Рекурсивно просматривает каталог и все его подкаталоги и возвращает список полных путей для всех повторяющихся файлов
# с заданным суффиксом(например,.mp3).

from pathlib import Path

duplicate_file_names = []
duplicate_file_paths = []
suf = ".mp3"


def find_duplicates_recursive(directory: Path) -> list:
    try:
        for child in directory.iterdir():
            if child.is_dir():
                # Функция вызывает себя только для подкаталогов - защита от беск рекурсии, когда функция будет самав себя входить
                find_duplicates_recursive(child)
            elif child.is_file() and child.suffix == suf:
                if child.name not in duplicate_file_names:
                    duplicate_file_names.append(child.name)
                else:
                    duplicate_file_paths.append(str(child.resolve()))

    except (PermissionError, FileNotFoundError):
        pass

    return duplicate_file_paths


find_duplicates_recursive(Path.cwd())
print(duplicate_file_paths)
