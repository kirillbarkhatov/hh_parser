from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    id: int  # уникальный идентификатор вакансии
    name: str  # название вакансии
    # location: str  # город, населенный пункт, область, страна
    # address: dict  # точный адрес работы (если указан)
    # salary: dict  # данные по зарплате, ключи "from", "to", "currency", "gross"
    # published_at: str  # дата публикации строкой вида "2024-08-04T18:37:39+0300"
    # url: str  # ссылка на вакансию
    # name_employer: str  # название работодателя
    # url_employer: str  # ссылка на страницу работодателя
    # schedule: str  # формат работы
    # employment: str  # занятость
    # experience: str  # опыт
    # requirement: str  # требования (кратко)
    # responsibility: str  # обязанности (кратко)

    def __init__(self, vacancy: dict) -> None:

        self.id = vacancy["id"]
        self.name = vacancy["name"]
        # self.location = vacancy["area"]["name"]
        # self.address = vacancy["address"]
        # self.salary = vacancy["salary"]
        # self.published_at = vacancy["published_at"]
        # self.url = vacancy["alternate_url"]
        # self.name_employer = vacancy["employer"]["name"]
        # self.url_employer = vacancy["employer"]["alternate_url"]
        # self.schedule = vacancy["schedule"]["name"]
        # self.employment = vacancy["employment"]["name"]
        # self.experience = vacancy["experience"]["name"]
        # self.requirement = vacancy["snippet"]["requirement"]
        # self.responsibility = vacancy["snippet"]["responsibility"]
        # print(self.name)

    def to_dict(self) -> dict:
        """Метод возвращает вакансию в формате словаря"""

        result = {
            "id": self.id,
            "name": self.name
        }
        return result

    @staticmethod
    def list_of_vacancies(vacancies: dict) -> list:
        """Создание списка из объектов класса Vacancy"""

        return [Vacancy(vacancy) for vacancy in vacancies]
