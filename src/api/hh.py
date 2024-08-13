import requests
from src.api.abc_parser import Parser
from typing import Any
from src.logger_decorators import func_call_logging


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    @staticmethod
    @func_call_logging
    def __connection_to_api(api_params: dict) -> Any:
        """Приватный метод для подключения к API"""

        url = 'https://api.hh.ru/vacancies'
        headers = {'User-Agent': 'HH-User-Agent'}

        response = requests.get(url, headers=headers, params=api_params)

        if response.status_code != 200:
            raise requests.RequestException
        return response

    @classmethod
    @func_call_logging
    def load_vacancies(cls, keyword: str) -> dict:
        """Метод для получения вакансий по ключевому слову"""

        params = {'text': keyword, 'page': 0, 'per_page': 100}
        vacancies = []

        # while params.get('page') != 20:
        while params.get('page') != 20:
            vacancies = cls.__connection_to_api(params).json()['items']
            vacancies.extend(vacancies)
            params['page'] += 1

        return vacancies
