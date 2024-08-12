from src.api.hh import HH
from src.vacancy_processing.vacancy import Vacancy
import json
from src.file_processing.json_saver import JSONSaver


# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HH()

# Получение вакансий с hh.ru в формате JSON
vacancies = HH.load_vacancies("Python")

print(vacancies[-1])
print(json.dumps(vacancies[-1], indent=4, ensure_ascii=False))

Vacancy(vacancies[-1])


print(Vacancy.list_of_vacancies(vacancies))
json_saver = JSONSaver()
json_saver.save_to_file(Vacancy.list_of_vacancies(vacancies))


# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
# # Пример работы контструктора класса с одной вакансией
# vacancy_processing = Vacancy("Python Developer", "", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy_processing)
# json_saver.delete_vacancy(vacancy_processing)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()

