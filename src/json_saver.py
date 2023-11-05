import json

from src.vacancy import Vacancy


class JSONSaver:
    """Класс записи и получения данных в директории json"""

    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def write_json(self, data):
        """Метод записи файла в директорию json"""

        with open(f"../json/{self.filename}.json", 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def read_json(self):
        """Метод получения данных из файла в директории json"""

        with open(f"../json/{self.filename}.json", 'rt', encoding="utf-8") as f:
            vacancies = json.load(f)

        all_vacancies = []

        for vacancy in vacancies:
            all_vacancies.append(Vacancy(
                vacancy["name"],
                vacancy["description"],
                vacancy["company_name"],
                vacancy["salary_from"],
                vacancy["salary_to"],
                vacancy["url"]
            ))

        return all_vacancies
