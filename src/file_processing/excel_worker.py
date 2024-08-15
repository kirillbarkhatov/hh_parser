import json
from typing import Any

import pandas as pd

from src.file_processing.abc_file_worker import FileWorker
from src.logger_decorators import func_call_logging
from src.vacancy_processing.vacancy import Vacancy


class ExcelWorker(FileWorker):
    """Класс для работы с json файлами"""

    __file_name: str  # имя файла
    path_to_file: str = "data/"  # путь до файла
    path_with_filename: str  # путь до файла вместе с именем файла

    @func_call_logging
    def __init__(self, file_name: str = "vacancies.xlsx") -> None:
        self.__file_name = self.__check_and_get_file_name(file_name)

    @func_call_logging
    def save_to_file(self, vacancies: list[dict]) -> None:
        """Метод для сохранения в файл списка вакансий"""

        vacancies_flat = pd.json_normalize(vacancies)

        # with open(self.path_to_file+self.__file_name, "w") as file:
        vacancies_flat.to_excel(self.path_to_file + self.__file_name)

    @func_call_logging
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

    @func_call_logging
    def get_from_file(self) -> Any:
        """Метод для получения данных из файла"""

        with open(self.path_to_file + self.__file_name, "r") as file:
            return json.load(file)

    @func_call_logging
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

    @func_call_logging
    def __check_and_get_file_name(self, file_name: str) -> str:
        if file_name[-5:] != ".xlsx":
            return f"{file_name}.xlsx"
        return file_name
