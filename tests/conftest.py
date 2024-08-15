import pytest


@pytest.fixture
def request_get():
    return {"items": [{"id": "93353083", "name": "Тестировщик комфорта квартир"}]}


@pytest.fixture
def load_vacancies_result():
    return [{"id": "93353083", "name": "Тестировщик комфорта квартир"} for _ in range(20)]