from unittest.mock import patch

import pytest
import requests

from src.api.hh import HH
from src.api.abc_parser import Parser


def test_load_vacancies(request_get, load_vacancies_result):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = request_get
        assert HH.load_vacancies("test") == load_vacancies_result


def test_load_vacancies_error():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 201
        with pytest.raises(requests.RequestException):
            HH.load_vacancies("test")


def test_abc_parser():
    """Вызов функций в абстрактных классах - вопрос наставнику: как протестировать приватный класс"""
    Parser.load_vacancies("test")
    # parser = Parser()
    # parser._Parser__connection_to_api({"text": "keyword", "page": 0, "per_page": 100})

