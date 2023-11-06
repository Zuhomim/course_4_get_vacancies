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
        return f'Название: {self.name}\nОписание: {self.description}\nЗарплата: {self.salary_from}\nСсылка: {self.url}'

    def __init__(self, name: str, description: str, company_name: str, salary_from: int, salary_to: int, url: str):
        self.name = name
        self.description = description
        self.company_name = company_name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url

    def __lt__(self, other):
        """Метод сравнения для сортировки списка вакансий"""

        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """Метод сравнения для сортировки списка вакансий"""

        return self.salary_from > other.salary_from

    def class_to_dict(self):
        """Метод подготовки свойств класса для записи в json-файл"""

        fields = {
            "name": self.name,
            "description": self.description,
            "company_name": self.company_name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "url": self.url
        }

        return fields
