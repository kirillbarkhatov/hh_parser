from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_vacancies(self, *args: Any, **kwargs: Any) -> Any:
        """Общий функционал для всех подклассов"""
        pass
