# Рекурсивно просматривает каталог и все его подкаталоги и возвращает список полных путей для всех повторяющихся файлов
# с заданным суффиксом(например,.mp3).

from pathlib import Path


def find_duplicates_recursive(directory: Path, duplicate_file_names=None, duplicate_file_paths=None) -> list:
    if duplicate_file_names is None:
        duplicate_file_names = []
    if duplicate_file_paths is None:
        duplicate_file_paths = []
    suf = ".mp3"
    try:
        for child in directory.iterdir():
            if child.is_dir():
                # Функция вызывает себя только для подкаталогов - защита от беск рекурсии, когда функция будет самав себя входить
                find_duplicates_recursive(child, duplicate_file_names, duplicate_file_paths)
            elif child.is_file() and child.suffix == suf:
                if child.name not in duplicate_file_names:
                    duplicate_file_names.append(child.name)
                else:
                    duplicate_file_paths.append(str(child.resolve()))

    except (PermissionError, FileNotFoundError):
        pass

    return duplicate_file_paths


print(find_duplicates_recursive(Path.cwd()))

