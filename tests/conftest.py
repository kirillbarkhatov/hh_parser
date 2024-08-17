import pytest
import json

from src.api.hh import HH
from src.api.abc_parser import Parser
from src.vacancy_processing.vacancy import Vacancy


@pytest.fixture
def request_get():
    return {"items": [{"id": "93353083", "name": "Тестировщик комфорта квартир"}]}


@pytest.fixture
def load_vacancies_result():
    return [{"id": "93353083", "name": "Тестировщик комфорта квартир"} for _ in range(20)]


@pytest.fixture
def short_vacancy():
    return {"id": "93353083", "name": "Тестировщик комфорта квартир"}


@pytest.fixture
def vacancies():
    with open("tests/vacancies_example.json", "r") as test_data:
        return json.load(test_data)["items"]


@pytest.fixture()
def vacancy(vacancies):
    return Vacancy(Vacancy.vacancies_from_hh_processing(vacancies)[0])
