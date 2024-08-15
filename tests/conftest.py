import pytest
import json

from src.api.hh import HH
from src.api.abc_parser import Parser


@pytest.fixture
def request_get():
    return {"items": [{"id": "93353083", "name": "Тестировщик комфорта квартир"}]}


@pytest.fixture
def load_vacancies_result():
    return [{"id": "93353083", "name": "Тестировщик комфорта квартир"} for _ in range(20)]


@pytest.fixture
def vacancies():
    with open("tests/vacancies_example.json", "r") as test_data:
        return json.load(test_data)["items"]
