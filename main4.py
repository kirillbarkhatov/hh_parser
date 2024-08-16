from src.file_processing.excel_worker import ExcelWorker
from src.vacancy_processing.vacancy import Vacancy
from src.api.hh import HH


obj = ExcelWorker("qwerty.xlsx")

# obj.get_from_file()

vacancies = HH.load_vacancies("кассир")
# obj.save_to_file(Vacancy.list_of_dicts_vacancies(vacancies))

print(vacancies[0])

v_hh = Vacancy.vacancies_from_hh_processing(vacancies)

print(v_hh[2])
