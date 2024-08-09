from typing import Any

from src.file_processing.file_worker import FileWorker

import json


class JSONSaver(FileWorker):
    """Класс для работы с json файлами"""
    file_path: str  # путь к файлу

    def __init__(self, file_path: str = "data/vacancies.json") -> None:
        self.file_path = file_path

    def save_to_file(self, vacancies) -> None:
        """Метод для сохранения в файл списка вакансий"""

        # кажется, этот функционал нужно перенести в Vacancy
        list_of_vacancies = []
        for vacancy in vacancies:
            list_of_vacancies.append(vacancy.to_dict())

        with open(self.file_path, "w") as file:
            json.dump(list_of_vacancies, file, indent=4, ensure_ascii=False)

    def add_to_file(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def get_from_file(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def delete_from_file(self, *args: Any, **kwargs: Any) -> Any:
        pass