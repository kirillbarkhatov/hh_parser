from abc import ABC, abstractmethod


class VacancyWorker(ABC):
    """Абстрактный класс, предъявляющий требования к подклассам, работающими с вакансиями"""

    @abstractmethod
    def to_dict(self) -> dict:
        """Метод возвращает вакансию в формате словаря"""

        pass

    @staticmethod
    @abstractmethod
    def get_list_of_vacancies(vacancies: dict) -> list:
        """Создание списка из объектов класса Vacancy"""

        pass

    @staticmethod
    @abstractmethod
    def get_list_of_dicts_vacancies(vacancies: dict) -> list:
        """Создание списка словарей из списка объектов вакансий"""

        pass

    @staticmethod
    @abstractmethod
    def get_list_id_vacancies(vacancies: list[dict]) -> list:
        """Получить список ID из списка вакансий"""

        pass

    @abstractmethod
    def get_salary(self) -> str:
        """Получить значение зарплаты"""

        pass
