from src.api.hh import HH
from src.file_processing.excel_worker import ExcelWorker
from src.file_processing.json_worker import JSONWorker
from src.utils import file_data_info
from src.vacancy_processing.vacancy import Vacancy


class UI:

    @staticmethod
    def greeting() -> None:
        """Функция приветствия"""

        print("Программа для получения вакансий с сайта hh.ru и работы с ними")
        print("Выберите действие:")
        print("1. Загрузить данные о вакансиях с сайта hh.ru по ключевому слову")
        print('2. Получить информацию о ранее загруженных данных (хранятся в "data/"')
        choice = 0
        while choice not in [1, 2]:
            choice = int(input("Введите 1 или 2: "))
            if choice not in [1, 2]:
                print("Повторите ввод")

        match choice:
            case 1:
                UI.get_hh_vacancy()
            case 2:
                file_data_info()

    @staticmethod
    def get_hh_vacancy() -> None:
        """Функция интерфейса для выбора опций загрузки данных о вакансиях"""

        query_key_word = input("Введите ключевое слово для запроса: ")
        print("Выберете формат файла в которых нужно сохранить полученные вакансии: ")
        print("1. json")
        print("2. csv")
        print("3. excel")
        print("4. txt")

        file_format = 0
        while file_format not in [1, 2, 3, 4]:
            file_format = int(input("Введите цифру от 1 до 4 для выбора формата файла: "))
            if file_format not in [1, 2, 3, 4]:
                print("Повторите ввод")

        file_name = input("Введите желаемое имя файла или пропустите ввод (имя по умолчанию - vacancies: ")

        vacancies = HH.load_vacancies(query_key_word)
        match file_format:
            case 1:
                json_saver = JSONWorker(file_name)
                json_saver.save_to_file(Vacancy.list_of_dicts_vacancies(vacancies))
                print(f"Данные успешно сохранены в файл {file_name}.json")

            case 2:
                json_saver = JSONWorker(file_name)
                json_saver.save_to_file(Vacancy.list_of_dicts_vacancies(vacancies))
                print(f"Данные успешно сохранены в файл {file_name}.csx")

            case 3:
                excel_saver = ExcelWorker(file_name)
                excel_saver.save_to_file(Vacancy.list_of_dicts_vacancies(vacancies))
                print(f"Данные успешно сохранены в файл {file_name}.xlsx")

            case 4:
                json_saver = JSONWorker(file_name)
                json_saver.save_to_file(Vacancy.list_of_dicts_vacancies(vacancies))
                print(f"Данные успешно сохранены в файл {file_name}.txt")
