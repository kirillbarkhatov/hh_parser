from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @staticmethod
    @abstractmethod
    def __connection_to_api(api_params: dict) -> object:
        """Общий функционал подключения к внешнему API для всех подклассов"""
        pass

    @staticmethod
    @abstractmethod
    def load_vacancies(keywords: str) -> dict:
        """Общий функционал для загрузки данных о вакансиях всех подклассов"""
        pass

