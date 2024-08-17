import json
from typing import Any

import pandas as pd

from src.file_processing.abc_file_worker import FileWorker
from src.logger_decorators import func_call_logging



class ExcelWorker(FileWorker):
    """Класс для работы с json файлами"""

    __file_name: str  # имя файла
    path_to_file: str = "data/"  # путь до файла
    path_with_filename: str  # путь до файла вместе с именем файла

    # @func_call_logging
    def __init__(self, file_name: str = "vacancies.xlsx") -> None:
        self.__file_name = self.__check_and_get_file_name(file_name)

    # @func_call_logging
    def save_to_file(self, vacancies: list[dict]) -> None:
        """Метод для сохранения в файл списка вакансий"""

        pd.DataFrame(vacancies).to_excel(self.path_to_file + self.__file_name, index=False)

    # @func_call_logging
    def add_to_file(self, vacancies: list[dict]) -> None:
        """Метод для добавления в файл вакансий без дублирования"""

        vacancies_in_file = pd.read_excel(self.path_to_file + self.__file_name)
        vacancies_in_file["id"] = vacancies_in_file["id"].astype(str)
        vacancies_to_add = pd.DataFrame(vacancies)
        vacancies_to_file = pd.concat([vacancies_in_file, vacancies_to_add], ignore_index=True).drop_duplicates(subset=["id"])
        vacancies_to_file.to_excel(self.path_to_file + self.__file_name, index=False)


    @func_call_logging
    def get_from_file(self) -> Any:
        """Метод для получения данных из файла"""

        df = pd.read_excel(self.path_to_file + self.__file_name)
        return df.to_dict(orient="records")


    # @func_call_logging
    def delete_from_file(self) -> None:
        """Удаляет все данные из файла"""

        pd.DataFrame().to_excel(self.path_to_file + self.__file_name, index=False)

    # @func_call_logging
    def __check_and_get_file_name(self, file_name: str) -> str:
        if file_name[-5:] != ".xlsx":
            return f"{file_name}.xlsx"
        return file_name
