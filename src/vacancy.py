class Vacancy:
    """Класс вакансии, включающий атрибуты:
        name - Наименование вакансии,
        description - Описание вакансии,
        company_name - Название организации,
        salary_from - Базовая зарплата,
        salary_to - Максимальная зарплата,
        url - ссылка на вакансию"""

    __slots__ = ['name', 'description', 'company_name', 'salary_from', 'salary_to', 'url']

    def __repr__(self):
        return (f'Vacancy(Name: {self.name}, Description: {self.description}, Company: {self.company_name},'
                f'Salary: {self.salary_from}, URL: {self.url})')

    def __str__(self):
        return f'Название: {self.name}\nОписание: {self.description}\nЗарплата: {self.salary_from}'

    def __init__(self, name, description, company_name, salary_from, salary_to, url):
        self.name = name
        self.description = description
        self.company_name = company_name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from
