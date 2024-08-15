from src.vacancy_processing.vacancy import Vacancy
from src.vacancy_processing.abc_vacancy_worker import VacancyWorker
import pytest

from unittest.mock import patch


def test_vacancy_base(vacancies):
    """Тест базового функционала класса, через методы list_of_vacancies и get_salary"""

    assert Vacancy.list_of_vacancies(vacancies)[0].get_salary() == "От 350000 до 450000"
    assert Vacancy.list_of_vacancies(vacancies)[5].get_salary() == "Зарплата не указана"
    assert Vacancy.list_of_vacancies(vacancies)[6].get_salary() == "От 800"
    assert Vacancy.list_of_vacancies(vacancies)[19].get_salary() == "До 100000"


def test_vacancy_dicts(vacancies):
    """Тесты методов создания словарей из объектов класса"""

    assert Vacancy.list_of_vacancies(vacancies)[0].to_dict()["name"] == "Тестировщик комфорта квартир"
    assert Vacancy.list_of_dicts_vacancies(vacancies)[0]["name"] == "Тестировщик комфорта квартир"
    assert Vacancy.list_id_vacancies(vacancies)[0] == "93353083"


def test_comparison(vacancies):
    """Тесты методов сравнения"""

    vcncs = Vacancy.list_of_vacancies(vacancies)
    assert vcncs[0] > vcncs[5]
    assert vcncs[0] >= vcncs[5]
    assert vcncs[6] <= vcncs[19]
    assert vcncs[6] < vcncs[19]
    assert vcncs[0] != vcncs[5]
    assert vcncs[0] == vcncs[0]


def test_comparison_error(vacancies):
    """Тесты методов сравнения"""

    vcncs = Vacancy.list_of_vacancies(vacancies)
    with pytest.raises(TypeError):
        assert vcncs[0] > "1"
    with pytest.raises(TypeError):
        assert vcncs[0] >= "1"
    with pytest.raises(TypeError):
        assert vcncs[6] <= "1"
    with pytest.raises(TypeError):
        assert vcncs[6] < "1"
    with pytest.raises(TypeError):
        assert vcncs[0] != "1"
    with pytest.raises(TypeError):
        assert vcncs[0] == "1"


def test_vacancy_worker(vacancies):
    """ до 100% базовый абстрактный класс - вопрос наставнику: как закрыть тестом метод объекта класса"""

    # vacancy = Vacancy()
    VacancyWorker.list_of_vacancies({})
    VacancyWorker.list_id_vacancies([])
    VacancyWorker.list_of_dicts_vacancies({})
    # vacancy.to_dict()
    # vacancy.get_salary()

    with patch("src.vacancy_processing.abc_vacancy_worker.VacancyWorker.to_dict") as mock_method:
        mock_method.return_value = {}
        VacancyWorker.to_dict()


