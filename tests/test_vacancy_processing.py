from src.vacancy_processing.vacancy import Vacancy
from src.vacancy_processing.abc_vacancy_worker import VacancyWorker
import pytest

from unittest.mock import patch


def test_vacancy_base(vacancies):
    """Тест базового функционала класса, через методы list_of_vacancies и get_salary"""

    vacancies = Vacancy.vacancies_from_hh_processing(vacancies)
    assert Vacancy.get_list_of_vacancies(vacancies)[0].get_salary() == "От 350000 до 450000"
    assert Vacancy.get_list_of_vacancies(vacancies)[5].get_salary() == "Зарплата не указана"
    assert Vacancy.get_list_of_vacancies(vacancies)[6].get_salary() == "От 800"
    assert Vacancy.get_list_of_vacancies(vacancies)[19].get_salary() == "До 100000"


def test_vacancy_dicts(vacancies):
    """Тесты методов создания словарей из объектов класса"""

    vacancies = Vacancy.vacancies_from_hh_processing(vacancies)
    assert Vacancy.get_list_of_vacancies(vacancies)[0].to_dict()["name"] == "Тестировщик комфорта квартир"
    vacancies = Vacancy.get_list_of_vacancies(vacancies)
    assert Vacancy.get_list_of_dicts_vacancies(vacancies)[0]["name"] == "Тестировщик комфорта квартир"
    assert Vacancy.get_list_id_vacancies(vacancies)[0] == "93353083"


def test_comparison(vacancies):
    """Тесты методов сравнения"""

    vacancies = Vacancy.vacancies_from_hh_processing(vacancies)
    vcncs = Vacancy.get_list_of_vacancies(vacancies)
    assert vcncs[0] > vcncs[5]
    assert vcncs[0] >= vcncs[5]
    assert vcncs[6] <= vcncs[19]
    assert vcncs[6] < vcncs[19]
    assert vcncs[0] != vcncs[5]
    assert vcncs[0] == vcncs[0]


def test_comparison_error(vacancies):
    """Тесты методов сравнения"""

    vacancies = Vacancy.vacancies_from_hh_processing(vacancies)
    vcncs = Vacancy.get_list_of_vacancies(vacancies)
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


def test_vacancy_without_attribute(short_vacancy):
    """Тест создания вакансий с неполным набором аттрибутов"""

    assert not Vacancy(short_vacancy).location


def test_str_vacancy(vacancy):
    """Тест метода str"""

    assert str(vacancy) == "Тестировщик комфорта квартир                                 - Зарплата: От 350000 до 450000  - Город: Воронеж              - График: Гибкий график"


def test_get_top_salary_vacancies(vacancies):
    """Тестируем топ по зарплате"""

    v_lst = Vacancy.vacancies_from_hh_processing(vacancies)
    v_obj = Vacancy.get_list_of_vacancies(v_lst)
    v_obj = Vacancy.filter_by_keywords(v_obj, ["Java"])
    assert Vacancy.get_top_salary_vacancies(v_lst, 1)[0]["salary"] == 4000000
    assert Vacancy.get_top_salary_vacancies(v_obj, 1)[0].salary == 4000000


def test_vacancy_worker(vacancies):
    """ до 100% базовый абстрактный класс - вопрос наставнику: как закрыть тестом метод объекта класса"""

    # vacancy = Vacancy()
    VacancyWorker.get_list_of_vacancies({})
    VacancyWorker.get_list_id_vacancies([])
    VacancyWorker.get_list_of_dicts_vacancies({})
    # vacancy.to_dict()
    # vacancy.get_salary()

    with patch("src.vacancy_processing.abc_vacancy_worker.VacancyWorker.to_dict") as mock_method:
        mock_method.return_value = {}
        VacancyWorker.to_dict()


