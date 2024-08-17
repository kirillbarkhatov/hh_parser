from numpy.random import vonmises

from src.api.hh import HH
from src.file_processing.excel_worker import ExcelWorker
from src.file_processing.json_worker import JSONWorker
from src.utils import file_data_info
from src.vacancy_processing.vacancy import Vacancy
from tests.conftest import vacancies
from typing import Any


class UI:

    @staticmethod
    def lets_go() -> None:
        """Функция запускающая программу"""

        print("Программа для получения вакансий с сайта hh.ru и работы с ними")
        print("Выберите действие:")
        print("1. Загрузить данные о вакансиях с сайта hh.ru по ключевому слову")
        print('2. Получить информацию о ранее загруженных данных (хранятся в "data/", поддерживаемые форматы: json, xlsx)')
        choice = 0

        while choice not in [1, 2]:
            try:
                choice = int(input("Введите 1 или 2: "))
                if choice not in [1, 2]:
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        print()
        match choice:
            case 1:
                UI.get_hh_vacancy()
            case 2:
                UI.files_info_and_choice()

    @staticmethod
    def get_hh_vacancy() -> Any:
        """Функция интерфейса для выбора опций загрузки данных о вакансиях c сайта hh.ru"""

        query_key_word = input("Введите ключевое слово для запроса: ")
        vacancies = HH.load_vacancies(query_key_word)
        vacancies_list = Vacancy.vacancies_from_hh_processing(vacancies)
        vacancies_objects = Vacancy.get_list_of_vacancies(vacancies_list)
        if len(vacancies_objects) == 0:
            print()
            print("Вакансий по вашему запросу не найдено, попробуйте снова")
            return UI.get_hh_vacancy()
        print()
        print(f"Количество загруженных вакансий - {len(vacancies_objects)}")
        print()
        return UI.vacancies_working(vacancies_objects)

    @staticmethod
    def files_info_and_choice() -> None:
        """Получение и вывод данных о файлах"""

        files = file_data_info()
        if len(files) == 0:
            print("Доступные для работы файлы отсутствуют")
        else:
            print("Для дальнейшей работы доступны следующие файлы: ")
            for i in range(len(files)):
                print(f"{i + 1}. {files[i]}")
            file_for_work = input("Введите имя требуемого файла: ")
            UI.file_working(file_for_work)


    @staticmethod
    def file_working(file_name: str) -> Any:
        """Функция интерфейса для выбора опций загрузки данных о вакансиях из файла"""

        if file_name[-5:] == ".json":
            file_worker = JSONWorker(file_name)
        elif file_name[-5:] == ".xlsx":
            file_worker = ExcelWorker(file_name)
        else:
            print("Неверно введено имя файла")
            return UI.files_info_and_choice()

        print("Доступные действия: ")
        print("1. Загрузить все вакансии из файла")
        print("2. Очистить файл")
        choice = int(input("Выберите 1 или 2: "))
        if choice == 1:
            vacancies_list = file_worker.get_from_file()
            vacancies_objects = Vacancy.get_list_of_vacancies(vacancies_list)
            print(f"Количество загруженных вакансий - {len(vacancies_objects)}")
            return UI.vacancies_working(vacancies_objects)

        elif choice == 2:
            file_worker.delete_from_file()
            print("Файл очищен")
            return UI.files_info_and_choice()

        else:
            return UI.file_working(file_name)

    @staticmethod
    def vacancies_working(vacancies: list) -> None:
        """Обработка списка вакансий"""

        print(f"Количество вакансий в работе - {len(vacancies)}")
        print("Доступны следующие действия для обработки списка вакансий:")
        print("1. Cохранить в файл")
        print("2. Отфильтровать топ вакансий по зарплате")
        print("3. Отфильтровать вакансии по ключевым словам")
        print("4. Вывести краткую информацию о вакансиях в консоль")
        choice = 0
        while choice not in [1, 2, 3, 4]:
            try:
                choice = int(input("Введите цифру от 1 до 4 для выбора действия: "))

                if choice not in [1, 2, 3, 4]:
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        match choice:

            case 1:
                UI.save_to_file(vacancies)

            case 2:
                while True:
                    try:
                        n = int(input("Введите количество вакансий с максимальной зарплатой, которые надо отобрать из списка: "))
                        break
                    except ValueError:
                        print("Повторите ввод - укажите целое число")
                if n == 0:
                    print()
                    print("Вы ввели 0 - так не останется вакансий для обработки. Давайте попробуем ещё раз")
                    print()
                    return UI.vacancies_working(vacancies)
                top_vacancies = Vacancy.get_top_salary_vacancies(vacancies, n)
                return UI.vacancies_working(top_vacancies)

            case 3:
                keyword_list = input("Введите ключевые слова для фильтрации через пробел: ").strip().split()
                filtered_vacancy = Vacancy.filter_by_keywords(vacancies, keyword_list)
                if len(filtered_vacancy) == 0:
                    print()
                    print("Ваш запрос не дал результата. Давайте попробуем ещё раз")
                    print()
                    return UI.vacancies_working(vacancies)
                return UI.vacancies_working(filtered_vacancy)

            case 4:
                for vacancy in vacancies:
                    print(vacancy)
                print()
                return UI.vacancies_working(vacancies)

    @staticmethod
    def save_to_file(vacancies: list) -> None:
        """Функция интерфейса для выбора опций сохранения данных в файл"""

        print("Выберете формат файла в которых нужно сохранить полученные вакансии: ")
        print("1. json")
        print("2. excel")

        file_format = 0
        while file_format not in [1, 2]:
            try:
                file_format = int(input("Введите цифру 1 или 2 для выбора формата файла: "))
                if file_format not in [1, 2]:
                    print("Повторите ввод")
            except ValueError:
                print("Повторите ввод")

        file_name = input("Введите желаемое имя файла или пропустите ввод (имя по умолчанию - vacancies): ")
        vacancies_to_save = Vacancy.get_list_of_dicts_vacancies(vacancies)
        match file_format:
            case 1:
                if len(file_name) > 0:
                    json_saver = JSONWorker(file_name)
                else:
                    json_saver = JSONWorker()
                json_saver.save_to_file(vacancies_to_save)
                print(f"Данные успешно сохранены в файл {file_name}.json")

            case 2:
                if len(file_name) > 0:
                    excel_saver = ExcelWorker(file_name)
                else:
                    excel_saver = ExcelWorker()
                excel_saver.save_to_file(vacancies_to_save)
                print(f"Данные успешно сохранены в файл {file_name}.xlsx")
