"""Функции."""


def get_file_text(file_path: str):
    """Получить текст файла по его пути."""
    with open(file_path, encoding="utf-8") as file:
        return file.read()
