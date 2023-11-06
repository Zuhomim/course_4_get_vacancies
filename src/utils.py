def sort_vacancies(vacancies):
    """Возвращает список вокансий по убыванию зарплаты (salary_from)"""

    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_top_vacancies(vacancies, top_n):
    """Возвращает топ позиций с максимальной зарплатой в кол-ве top_n"""

    vacancies = sort_vacancies(vacancies)
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """Выводит в консоль каждую вакансию из списка вакансий"""

    for vacancy in vacancies:
        print(vacancy)
        print("-" * 150)
