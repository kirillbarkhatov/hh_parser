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
    def list_of_vacancies(vacancies: dict) -> Any:
        """Общий функционал для списка из всех объектов класса"""

        pass
