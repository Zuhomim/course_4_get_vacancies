import json
import os
from src.vacancy import Vacancy


class JSONSaver:
    """Класс записи и получения данных в директории json"""

    @staticmethod
    def write_json(data):
        """Метод записи файла в директорию json"""

        with open(f"../json/vacancies.json", 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def read_json():
        """Метод получения данных из файла в директории json"""

        with open(f"../json/vacancies.json", 'rt', encoding="utf-8") as f:
            vacancies = json.load(f)

        return vacancies

    @staticmethod
    def get_vacancies():
        """Метод получения списка вакансий"""

        all_vacancies = []
        vacancies = JSONSaver.read_json()
        for vacancy_item in vacancies:
            all_vacancies.append(Vacancy(
                vacancy_item["name"],
                vacancy_item["description"],
                vacancy_item["company_name"],
                vacancy_item["salary_from"],
                vacancy_item["salary_to"],
                vacancy_item["url"]
            ))

        return all_vacancies

    def add_vacancy(self, vacancy: Vacancy):
        """Метод добавления вакансии в список вакансий"""

        all_vacancies = []
        vacancy_to_json = {
                    "name": vacancy.name if vacancy.name else "",
                    "description": vacancy.description if vacancy.description else "",
                    "company_name": vacancy.company_name if vacancy.company_name else "",
                    "salary_from": vacancy.salary_from if vacancy.salary_from else 0,
                    "salary_to": vacancy.salary_to if vacancy.salary_to else 0,
                    "url": vacancy.url if vacancy.url else ""
                }

        if os.path.exists("../json/vacancies.json"):
            all_vacancies = self.read_json()
            all_vacancies.append(vacancy_to_json)
        else:
            all_vacancies.append(vacancy_to_json)
            self.write_json(vacancy_to_json)

        self.write_json(all_vacancies)

    def delete_vacancy(self, vacancy_to_del: Vacancy):
        """Метод удаления вакансии из списка вакансий"""

        all_vacancies = self.get_vacancies()

        data = [vacancy.class_to_dict() for vacancy in all_vacancies if (
                    vacancy.name != vacancy_to_del.name
                    or vacancy.company_name != vacancy_to_del.company_name
                    or vacancy.salary_from != vacancy_to_del.salary_from
        )]

        self.write_json(data)

    def get_vacancies_by_salary(self, salary_range: str):
        """Метод вывода вакансий по желаемой зарплате / диапазону зарплат"""

        all_vacancies = []
        salary_to = 0
        vacancies = self.get_vacancies()

        if "-" in salary_range:
            salary_from = int(salary_range.split("-")[0].replace(" ", ""))
            salary_to = int(salary_range.split("-")[1].replace(" ", ""))
        else:
            salary_from = int(salary_range.replace(" ", ""))

        for vacancy in vacancies:
            if salary_to > 0:
                if salary_from <= vacancy.salary_from <= salary_to:
                    all_vacancies.append(vacancy)
            else:
                if salary_from <= vacancy.salary_from:
                    all_vacancies.append(vacancy)

        return all_vacancies
