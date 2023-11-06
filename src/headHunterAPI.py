import requests

from src.engine import Engine


class HeadHunterAPI(Engine):
    """Класс получения вакансий по API HH.ru"""
    def __init__(self):
        pass

    def get_request(self, keyword, count_page):
        """Метод получения вакансий по API hh.ru"""

        params = {
            "page": 0,
            "per_page": 50,
            "text": keyword.lower(),
        }
        all_vacancies = []
        vacancies = requests.get("https://api.hh.ru/vacancies", params=params).json()["items"]

        for i in range(count_page):
            params["page"] = i
            all_vacancies.extend(vacancies)

        return all_vacancies

    def get_vacancies(self, keyword, count_page=5):
        all_vacancies = []
        vacancies = self.get_request(keyword.lower(), count_page)
        for vacancy in vacancies:
            if vacancy["salary"]:
                salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            else:
                salary_from = 0
                salary_to = 0

            all_vacancies.append({
                "name": vacancy["name"],
                "description": vacancy["snippet"]["responsibility"],
                "company_name": vacancy["employer"]["name"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "url": vacancy["alternate_url"]
            })

        return all_vacancies

    def get_filtered_vacancies(self):
        pass
