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

    def save_to_file(self, vacancies: list[dict]) -> None:
        """Метод для сохранения в файл списка вакансий"""

        with open(self.path_to_file+self.__file_name, "w") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def add_to_file(self, vacancies: list[dict]) -> None:
        """Метод для добавления в файл вакансий без дублирования"""

        vacancies_in_file = self.get_from_file()
        ids_vacancies = Vacancy.list_id_vacancies(vacancies)
        ids_vacancies_in_file = Vacancy.list_id_vacancies(vacancies_in_file)

        print(ids_vacancies)
        print(ids_vacancies_in_file)
        add_id_vacancies = list(set(ids_vacancies).difference(set(ids_vacancies_in_file)))
        print(add_id_vacancies)
        for vacancy_id in add_id_vacancies:
            i = ids_vacancies.index(vacancy_id)
            vacancies_in_file.append(vacancies[i])

        print(len(vacancies_in_file))
        self.save_to_file(vacancies_in_file)

        # add_vacancies = list(set(vacancies).difference(set(vacancies_in_file)))
        # vacancies_in_file.extend(add_vacancies)
        # self.save_to_file(vacancies_in_file)

    def get_from_file(self) -> list[dict]:
        """Метод для получения данных из файла"""

        with open(self.path_to_file+self.__file_name, "r") as file:
            return json.load(file)

    def delete_from_file(self, list_id_vacancies: list[str] | None = None) -> None:
        """Общий функционал для удаления данных из файла"""

        if not list_id_vacancies:
            with open(self.path_to_file + self.__file_name, "w") as file:
                json.dump(None, file, indent=4, ensure_ascii=False)

        else:
            vacancies = self.get_from_file()
            i = 0
            while i != len(vacancies):
                if vacancies[i]["id"] in list_id_vacancies:
                    vacancies.pop(i)
                    continue
                i += 1
            self.save_to_file(vacancies)