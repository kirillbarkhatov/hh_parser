from typing import Any

from src.file_processing.abc_file_worker import FileWorker
from src.vacancy_processing.vacancy import Vacancy

import json


class JSONWorker(FileWorker):
    """Класс для работы с json файлами"""
    __file_name: str  # имя файла
    path_to_file: str = "data/"  # путь до файла
    path_with_filename: str  # путь до файла вместе с именем файла

    def __init__(self, file_name: str = "vacancies.json") -> None:
        self.__file_name = file_name

    def save_to_file(self, vacancies) -> None:
        """Метод для сохранения в файл списка вакансий"""

        # кажется, этот функционал нужно перенести в Vacancy
        # list_of_vacancies = []
        # for vacancy in vacancies:
        #     list_of_vacancies.append(vacancy.to_dict())

        with open(self.path_to_file+self.__file_name, "w") as file:
            json.dump(Vacancy.list_of_dicts_vacancies(vacancies), file, indent=4, ensure_ascii=False)

    def add_to_file(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def get_from_file(self, *args: Any, **kwargs: Any) -> Any:
        pass

    def delete_from_file(self, *args: Any, **kwargs: Any) -> Any:
        pass