from typing import Any

from src.logger_decorators import func_call_logging
from src.vacancy_processing.abc_vacancy_worker import VacancyWorker


class Vacancy(VacancyWorker):
    """Класс для работы с вакансиями"""

    id: int  # уникальный идентификатор вакансии
    name: str  # название вакансии
    location: str  # город, населенный пункт, область, страна
    address: dict  # точный адрес работы (если указан)  - сложная вложенность - отказываюсь
    salary: float # Приведенное значение зарплаты для сравнения
    salary_string: str # Диапазон или комментарий по зарплате
    # salary: dict  # данные по зарплате, ключи "from", "to", "currency", "gross" - сложная вложенность - отказываюсь
    published_at: str  # дата публикации строкой вида "2024-08-04T18:37:39+0300"
    url: str  # ссылка на вакансию
    name_employer: str  # название работодателя
    # url_employer: str  # ссылка на страницу работодателя - появилась ошибка после добавления excel
    schedule: str  # формат работы
    employment: str  # занятость
    experience: str  # опыт
    requirement: str  # требования (кратко)
    responsibility: str  # обязанности (кратко)

    # набор, от которого отказался
    # __slots__ = ("id", "name", "location", "address", "salary", "published_at", "url", "name_employer",
    # "url_employer", "schedule", "employment", "experience", "requirement", "responsibility")
    __slots__ = (
        "id",
        "name",
        "location",
        "salary",
        "salary_string",
        "published_at",
        "url",
        "name_employer",
        "schedule",
        "employment",
        "experience",
        "requirement",
        "responsibility",
    )

    @func_call_logging
    def __init__(self, vacancy: dict) -> None:
        """На вход конструктора ожидается словарь с ключами, аналогичными в __slots__
        В классе реализованы методы, позволяющие обработать данные от hh для приведения их в нужный вид
        """

        for vacancy_attribute in self.__slots__:
            if self.__check_attribute(vacancy_attribute, vacancy.keys()):
                setattr(self, vacancy_attribute, vacancy[vacancy_attribute])
            else:
                setattr(self,vacancy_attribute, None)

    def __str__(self) -> str:
        """Получение краткой информации о вакансии"""

        return f"{(self.name + " " * 600)[:60]} - Зарплата: {(self.salary_string + " " * 20)[:20]} - Город: {(self.location + " " * 20)[:20]} - График: {self.schedule}"

    @func_call_logging
    def to_dict(self) -> dict:
        """Метод возвращает вакансию в формате словаря"""

        result = {}

        for attr in self.__slots__:
            result[attr] = getattr(self, attr)

        return result

    @staticmethod
    @func_call_logging
    def get_list_of_vacancies(vacancies: list[dict]) -> list:
        """Создание списка из объектов класса Vacancy"""

        return [Vacancy(vacancy) for vacancy in vacancies]

    @staticmethod
    @func_call_logging
    def get_list_of_dicts_vacancies(vacancies: list) -> list:
        """Создание списка словарей из списка объектов вакансий"""

        return [vacancy.to_dict() for vacancy in vacancies]

    @func_call_logging
    def __check_attribute(self, attribute: Any, keys: list) -> Any:
        """Валидация аттрибутов при создании объекта класса"""

        return attribute in keys

    @staticmethod
    @func_call_logging
    def get_list_id_vacancies(vacancies: list) -> list:
        """Получить список ID из списка вакансий (объектов или словарей)"""

        return [vacancy.id if isinstance(vacancy, Vacancy) else vacancy["id"] for vacancy in vacancies]

    @func_call_logging
    def get_salary(self) -> str:
        """Получить значение зарплаты"""

        return self.salary_string

    @func_call_logging
    def __get_salary_for_comparison(self) -> Any:
        """Получить значение зарплаты для сравнения. По умолчанию берется значение "от", если ничего не указано - 0"""

        return self.salary

    @func_call_logging
    def __eq__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для равенства =="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() == other.__get_salary_for_comparison()
        else:
            raise TypeError

    @func_call_logging
    def __ne__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для неравенства !="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() != other.__get_salary_for_comparison()
        else:
            raise TypeError

    @func_call_logging
    def __lt__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора меньше <"""
        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() < other.__get_salary_for_comparison()
        else:
            raise TypeError

    @func_call_logging
    def __le__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора меньше или равно <="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() <= other.__get_salary_for_comparison()
        else:
            raise TypeError

    @func_call_logging
    def __gt__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора больше >"""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() > other.__get_salary_for_comparison()
        else:
            raise TypeError

    @func_call_logging
    def __ge__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора больше или равно >="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() >= other.__get_salary_for_comparison()
        else:
            raise TypeError

    @staticmethod
    @func_call_logging
    def get_top_salary_vacancies(vacancies: list, top_n: int) -> list:
        """Получить топ вакансий по зарплате в заданном количестве"""

        if isinstance(vacancies[0], Vacancy):
            sorted_vacancies = sorted(vacancies, reverse=True)
        else:
            sorted_vacancies = sorted(vacancies, key=lambda x: x["salary"], reverse=True)

        return sorted_vacancies[:top_n]


    @staticmethod
    @func_call_logging
    def filter_by_keywords(vacancies: list, keywords: list) -> list:
        """Оставляет в списке только те вакансии, которые содержат ключевые слова в названии,
        требованиях или обязанностях
        """

        filtered_vacancies =[]
        for vacancy in vacancies:
            string_for_searching = (vacancy.name + str(vacancy.requirement) + str(vacancy.responsibility)).lower()
            check_status = True
            for keyword in keywords:
                if keyword.lower() in string_for_searching:
                    check_status *= True
                else:
                    check_status *= False
            if check_status:
                filtered_vacancies.append(vacancy)

        return filtered_vacancies


    @classmethod
    @func_call_logging
    def vacancies_from_hh_processing(cls, vacancies: list[dict]) -> list[dict]:
        """Приведение данных от hh к формату для дальнейшей обработки"""

        vacancies_processing = []
        for vacancy in vacancies:
            vacancy_processing = {}
            for key in cls.__slots__:
                vacancy_processing[key] = cls.__get_attribute_value_from_hh(key, vacancy)

            vacancies_processing.append(vacancy_processing)
        return vacancies_processing

    @staticmethod
    @func_call_logging
    def __get_attribute_value_from_hh(attribute: str, vacancy: dict) -> Any:
        """Привязка мест хранения аттрибутов в данных от hh"""

        match attribute:
            case "id":
                return vacancy["id"]

            case "name":
                return vacancy["name"]

            case "location":
                return vacancy["area"]["name"]

            # от адреса отказался
            # case "address":
            #     return vacancy["address"]

            case "salary":
                if not vacancy["salary"]:
                    return 0

                if not vacancy["salary"]["from"] and not vacancy["salary"]["to"]:
                    return 0

                if not vacancy["salary"]["from"]:
                    return vacancy["salary"]["to"]

                if not vacancy["salary"]["to"]:
                    return vacancy["salary"]["from"]

                return min(vacancy["salary"]["from"], vacancy["salary"]["to"])

            case "salary_string":
                if not vacancy["salary"]:
                    return "Зарплата не указана"

                if not vacancy["salary"]["from"] and not vacancy["salary"]["to"]:
                    return "Зарплата не указана"

                if not vacancy["salary"]["from"]:
                    return f"До {vacancy["salary"]["to"]}"

                if not vacancy["salary"]["to"]:
                    return f"От {vacancy["salary"]["from"]}"

                return f"От {vacancy["salary"]["from"]} до {vacancy["salary"]["to"]}"

            case "published_at":
                    return vacancy["published_at"]

            case "url":
                return vacancy["alternate_url"]

            case "name_employer":
                return vacancy["employer"]["name"]

            # Пока отказался
            # case "url_employer":
            #     return vacancy["employer"]["alternate_url"]

            case "schedule":
                return vacancy["schedule"]["name"]

            case "employment":
                return vacancy["employment"]["name"]

            case "experience":
                return vacancy["experience"]["name"]

            case "requirement":
                return vacancy["snippet"]["requirement"]

            case "responsibility":
                return vacancy["snippet"]["responsibility"]

            case _:
                return None
