import os

from src.file_processing.excel_worker import ExcelWorker
from src.file_processing.json_worker import JSONWorker
from src.logger_decorators import func_call_logging
from src.vacancy_processing.vacancy import Vacancy


@func_call_logging
def file_data_info() -> list:
    """Функция для получения данных о файлах в папке data"""

    path = "data/"
    files = []
    for dir_entry in os.scandir(path):
        if dir_entry.is_file():
            files.append(dir_entry.name)
    print(f"В папке {path} содержится {len(files)} файл(а)(ов):")
    checked_files = []
    for file in files:
        try:
            if file[-5:] == ".json":
                checking_file = JSONWorker(file)
            elif file[-5:] == ".xlsx":
                checking_file = ExcelWorker(file)
            else:
                raise TypeError
            file_data = checking_file.get_from_file()
            if len(file_data) == 0:
                raise TypeError
            vacancies = Vacancy.get_list_id_vacancies(file_data)
            checked_files.append(file)
            print(f"{file} - содержит {len(vacancies)} вакансий")
        except TypeError:
            print(f"{file} - файл не содержит данных о вакансиях или формат файла не поддерживается")
        except FileNotFoundError:
            print(f"{file} - файл не содержит данных о вакансиях или формат файла не поддерживается")

    return checked_files
