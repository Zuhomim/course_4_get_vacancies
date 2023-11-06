# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.headHunterAPI import HeadHunterAPI
from src.json_saver import JSONSaver
from src.super_job_api import SuperJobAPI
from src.utils import sort_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
super_job_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python", 5)
super_job_vacancies = super_job_api.get_vacancies("Python", 5)

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy(name="Python Developer", url="<https://hh.ru/vacancy/123456>", salary_from=150000,
                  description="Требования: опыт работы от 3 лет...", company_name="", salary_to=0)

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
print(json_saver.get_vacancies_by_salary("100 000-150 000 "))
print("-" * 150)
print_vacancies(json_saver.get_vacancies_by_salary("100 000-150 000 "))
json_saver.delete_vacancy(vacancy)


def get_vacancies():
    """Запускает поиск вакансий на платформах по API, записывает данные в vacancies.json"""

    platforms = ["HeadHunter", "SuperJob"]
    search_query = input(f"Введите поисковый запрос на платформах {platforms[0]} и {platforms[1]}: ")

    all_vacancies = []
    all_vacancies.extend(hh_api.get_vacancies(search_query))
    all_vacancies.extend(super_job_api.get_vacancies(search_query))

    if not all_vacancies:
        print("Нет вакансий по Вашему запросу")
        get_vacancies()
    else:
        json_saver.write_json(all_vacancies)


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    get_vacancies()

    while True:

        command_num = input(f"Введите номер команды для вывода: 1 - Вывод списка всех вакансий по убыванию ЗП,\n"
                            f"2 - Для вывода топ-10 вакансий,\n"
                            f"3 - Для вывода вакансий по желаемой зарплате,\n"
                            f"4 - Для нового поиска:\n"
                            f"5 - Для выхода из программы,\n")
        if command_num == "5":
            break
        elif command_num == "2":
            print_vacancies(get_top_vacancies(json_saver.get_vacancies(), 10))
        elif command_num == "1":
            print_vacancies(sort_vacancies(json_saver.get_vacancies()))
        elif command_num == "3":
            needed_salary = input(f"Пожалуйста, введите желаемую для поиска зарплату / диапазон:\n")
            print_vacancies(json_saver.get_vacancies_by_salary(needed_salary))
        elif command_num == "4":
            get_vacancies()
        else:
            print("Пожалуйста, введите другую команду")
            continue


if __name__ == "__main__":
    user_interaction()
