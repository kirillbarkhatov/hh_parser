from src.file_processing.excel_worker import ExcelWorker
from src.vacancy_processing.vacancy import Vacancy
from src.api.hh import HH


obj = ExcelWorker("qwerty.xlsx")

# obj.get_from_file()

vacancies = HH.load_vacancies("кассир")
# obj.save_to_file(Vacancy.list_of_dicts_vacancies(vacancies))

print(vacancies[0])

v_hh = Vacancy.vacancies_from_hh_processing(vacancies)

v_lst_obj = Vacancy.get_list_of_vacancies(v_hh)

print(Vacancy.get_list_id_vacancies(v_lst_obj))
print(Vacancy.get_list_id_vacancies(v_hh))
print(Vacancy.get_list_of_dicts_vacancies(v_lst_obj))
print(v_lst_obj[0].get_salary())
print(v_lst_obj[0] > v_lst_obj[1])
for i in Vacancy.get_top_salary_vacancies(v_lst_obj, 3):
    print(i.salary)
for i in Vacancy.get_top_salary_vacancies(v_hh, 3):
    print(i["salary"])

print(Vacancy.filter_by_keywords(v_lst_obj,["Галерея"]))

