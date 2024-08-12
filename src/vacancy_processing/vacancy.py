from typing import Any
from src.vacancy_processing.abc_vacancy_worker import VacancyWorker


class Vacancy(VacancyWorker):
    """Класс для работы с вакансиями"""

    id: int  # уникальный идентификатор вакансии
    name: str  # название вакансии
    location: str  # город, населенный пункт, область, страна
    address: dict  # точный адрес работы (если указан)
    salary: dict  # данные по зарплате, ключи "from", "to", "currency", "gross"
    published_at: str  # дата публикации строкой вида "2024-08-04T18:37:39+0300"
    url: str  # ссылка на вакансию
    name_employer: str  # название работодателя
    url_employer: str  # ссылка на страницу работодателя
    schedule: str  # формат работы
    employment: str  # занятость
    experience: str  # опыт
    requirement: str  # требования (кратко)
    responsibility: str  # обязанности (кратко)

    __slots__ = ("id", "name", "location", "address", "salary", "published_at", "url", "name_employer", "url_employer", "schedule", "employment", "experience", "requirement", "responsibility")

    def __init__(self, vacancy: dict) -> None:

        for vacancy_attribute in self.__slots__:
            if self.__check_attribute(vacancy_attribute):
                setattr(self, vacancy_attribute, self.__get_attribute_value(vacancy_attribute, vacancy))

    @staticmethod
    def __get_attribute_value(attribute: str, vacancy: dict) -> Any:
        """Привязка мест хранения аттрибутов к месту хранения в JSON"""

        match attribute:
            case "id":
                return vacancy["id"]
            case "name":
                return vacancy["name"]
            case "location":
                return vacancy["area"]["name"]
            case "address":
                return vacancy["address"]
            case "salary":
                return vacancy["salary"]
            case "published_at":
                return vacancy["published_at"]
            case "url":
                return vacancy["alternate_url"]
            case "name_employer":
                return vacancy["employer"]["name"]
            case "url_employer":
                return vacancy["employer"]["alternate_url"]
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

    def to_dict(self) -> dict:
        """Метод возвращает вакансию в формате словаря"""

        result = {}

        for attr in self.__slots__:
            result[attr] = getattr(self, attr)

        return result

    @staticmethod
    def list_of_vacancies(vacancies: dict) -> list:
        """Создание списка из объектов класса Vacancy"""

        return [Vacancy(vacancy) for vacancy in vacancies]

    def __check_attribute(self, attribute) -> Any:
        """Валидация аттрибутов при создании объекта класса"""

        return attribute in self.__slots__

    def get_salary(self) -> str:
        """Получить значение зарплаты"""

        if not self.salary:
            return "Зарплата не указана"

        if not self.salary["from"] and not self.salary["to"]:
            return "Зарплата не указана"

        if not self.salary["from"]:
            return f"До {self.salary["to"]}"

        if not self.salary["to"]:
            return f"От {self.salary["from"]}"

        return f"От {self.salary["from"]} до {self.salary["to"]}"

    def __get_salary_for_comparison(self) -> int:
        """Получить значение зарплаты для сравнения. По умолчанию берется значение "от", если ничего не указано - 0"""

        if not self.salary:
            return 0

        if not self.salary["from"] and not self.salary["to"]:
            return 0

        if not self.salary["from"]:
            return self.salary["to"]

        if not self.salary["to"]:
            return self.salary["from"]

        return min(self.salary["from"], self.salary["to"])

    def __eq__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для равенства =="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() == other.__get_salary_for_comparison()
        else:
            raise TypeError

    def __ne__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для неравенства !="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() != other.__get_salary_for_comparison()
        else:
            raise TypeError

    def __lt__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора меньше <"""
        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() < other.__get_salary_for_comparison()
        else:
            raise TypeError

    def __le__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора меньше или равно <="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() <= other.__get_salary_for_comparison()
        else:
            raise TypeError

    def __gt__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора больше >"""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() > other.__get_salary_for_comparison()
        else:
            raise TypeError

    def __ge__(self, other: Any) -> Any:
        """Метод сравнения вакансий по зарплате - для оператора больше или равно >="""

        if type(other) is Vacancy:
            return self.__get_salary_for_comparison() >= other.__get_salary_for_comparison()
        else:
            raise TypeError
