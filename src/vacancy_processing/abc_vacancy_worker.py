from abc import ABC, abstractmethod
from typing import Any


class VacancyWorker(ABC):
    """Абстрактный класс, предъявляющий требования к подклассам, работающими с вакансиями"""

    @abstractmethod
    def to_dict(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для получения данных в виде словаря"""

        pass

    @staticmethod
    @abstractmethod
    def list_of_vacancies(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для списка из всех объектов класса"""

        pass

    @abstractmethod
    def check_attribute(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для проверки атрибутов объекта класса"""

        pass

    @abstractmethod
    def salary_comparison(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для сравнения вакансий по зарплате"""

        pass

