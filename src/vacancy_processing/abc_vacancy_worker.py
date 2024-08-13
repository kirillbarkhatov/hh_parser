from abc import ABC, abstractmethod


class VacancyWorker(ABC):
    """Абстрактный класс, предъявляющий требования к подклассам, работающими с вакансиями"""

    @abstractmethod
    def to_dict(self) -> dict:
        """Метод возвращает вакансию в формате словаря"""

        pass

    @staticmethod
    @abstractmethod
    def list_of_vacancies(vacancies: dict) -> list:
        """Создание списка из объектов класса Vacancy"""

        pass

    @staticmethod
    @abstractmethod
    def list_of_dicts_vacancies(vacancies: dict) -> list:
        """Создание списка словарей из списка объектов вакансий"""

        pass

    @staticmethod
    @abstractmethod
    def list_id_vacancies(vacancies: list[dict]):
        """Получить список ID из списка вакансий"""

        pass

    @abstractmethod
    def get_salary(self) -> str:
        """Получить значение зарплаты"""

        pass

    @abstractmethod
    def __get_salary_for_comparison(self) -> int:
        """Получить значение зарплаты для сравнения. По умолчанию берется значение "от", если ничего не указано - 0"""

        pass
